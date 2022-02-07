# -*- coding: utf-8 -*-
# @Time     : 2022/1/17 15:16
# @File     : threads.py.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 线程函数

import os
import re
import jpype
import jieba
import requests
import importlib
import wordcloud
import traceback
import numpy as np
import pandas as pd
from PIL import Image
import jieba.posseg as posseg
import jieba.analyse as analyse
from collections import Counter
from PySide6.QtCore import QThread, Signal
from utils import GroupedColorFunc, config, start_jvm, built_version


# 检查更新
class CheckUpdateThread(QThread):
    endSignal = Signal(int)

    def __init__(self):
        super(CheckUpdateThread, self).__init__()
        self.new_version = None
        self.version_date = None
        self.update_info = None
        self.status_code = None
        self.download_link = None

    def run(self) -> None:
        try:
            res = requests.get('https://gitee.com/casuallyName/text-tools/raw/main/update_info.json', timeout=10)
            self.status_code = res.status_code
            if self.status_code == 200:
                info = res.json()
                if self.check_version(info['LatestVersion']):
                    self.new_version = f"V {info['LatestVersion']} "
                    self.version_date = f"Built on {info['LatestVersionBuiltDate']}"
                    if built_version in info['PatchPack']['PatchPackFor']:
                        self.download_link = info['PatchPack']['Link']
                    else:
                        self.download_link = info['DownLoad']['阿里云盘']
                    self.update_info = '<p>其他下载地址：' + ' | '.join(
                        [f"<a href='{v}'>{k}下载</a>" for k, v in info['DownLoad'].items()]) + '</p><p>'
                    for i in info['Content']:
                        self.update_info += f'· {i}<br>'
                    self.update_info = self.update_info + '</p>'
                    if built_version in info['PatchPack']['PatchPackFor']:
                        self.endSignal.emit(2)
                    else:
                        self.endSignal.emit(1)
                else:
                    self.endSignal.emit(0)
            else:
                self.endSignal.emit(-1)
        except:
            traceback.print_exc()
            self.endSignal.emit(-2)

    def check_version(self, new_v):
        new_v = str(new_v).split('.') + ['0', '0', '0']
        old_v = built_version.split('.') + ['0', '0', '0']
        for i in range(3):
            if new_v[i] > old_v[i]:
                return True
        return False


# 读取表格数据
class ReadFileThread(QThread):
    endSignal = Signal()

    def __init__(self, file_path, file_type):
        super(ReadFileThread, self).__init__()
        self.file_path = file_path
        self.file_type = file_type
        self.data = None

    def run(self) -> None:
        if self.file_type in ['所有 Excel 文件(*.xl*)', 'Excel 工作簿(*.xlsx)', 'Excel 97-2003(*.xls)']:
            self.data = pd.read_excel(self.file_path, sheet_name=None)
        elif self.file_type == 'CSV UTF-8 (逗号分隔) (*.csv)':
            self.data = {'Sheet1': pd.read_csv(self.file_path)}
        else:
            raise KeyError(f"'{self.file_type}'不是支持的读取类型")
        self.endSignal.emit()


# 读取图片
class ReadImageThread(QThread):
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, file_name, view_form):
        super(ReadImageThread, self).__init__()
        self.file_name = file_name
        self.view_form = view_form
        self.image = None

    def run(self) -> None:
        try:
            # img = Image.open(self.file_name)
            # self.image = np.array(img).copy()
            self.image = Image.open(self.file_name)
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())


# 保存表格数据
class WriteExcelThread(QThread):
    endSignal = Signal()
    errorSignal = Signal(str)

    def __init__(self, file_name, file_type, data_dict: dict):
        super(WriteExcelThread, self).__init__()
        self.file_name = file_name
        self.file_type = file_type
        self.data_dict = data_dict

    def run(self) -> None:
        try:
            if self.file_type == 'CSV UTF-8 (逗号分隔) (*.csv)':
                try:
                    self.data_dict[list(self.data_dict.keys())[0]].to_csv(self.file_name,
                                                                          index=False,
                                                                          encoding='utf-8-sig')
                except PermissionError:
                    self.errorSignal.emit(f"保存失败，保存文件'{self.file_name}'时被拒绝，文件可能被占用")
            else:
                try:
                    File = pd.ExcelWriter(self.file_name)
                    for sheet_name, data in self.data_dict.items():
                        data.to_excel(File, sheet_name=sheet_name, index=False)
                    File.close()
                except PermissionError:
                    self.errorSignal.emit(f"保存失败，保存文件'{self.file_name}'时被拒绝，文件可能被占用")
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())
            return


# 保存图片
class SaveImageThread(QThread):
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, save_func, file_path):
        super(SaveImageThread, self).__init__()
        # self.img = img.copy()
        self.save_func = save_func
        self.file_path = file_path

    def run(self) -> None:
        try:
            # self.img.save(self.file_path)
            self.save_func(self.file_path)
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())


# 文本清洗线程
class TextCleaningThread(QThread):
    barSignal = Signal(int)
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, args):
        super(TextCleaningThread, self).__init__()
        self.args = args

    def run(self) -> None:
        try:
            result = []
            bar = 0
            l = self.args.data.shape[0]
            for i, value in enumerate(self.args.data[self.args.input_column].values):
                result.append(self.args.join_symbol.join(re.findall(self.args.pattern, str(value))))
                if int((i + 1) / l * 90) != bar:
                    bar = int(i / l * 90)
                    self.barSignal.emit(bar)
            self.args.data[f'{self.args.input_column}_清洗结果'] = result
            self.barSignal.emit(100)
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())


# 文本挖掘线程
class TextMiningThread(QThread):
    barSignal = Signal(int)
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, args):
        super(TextMiningThread, self).__init__()
        self.args = args
        self.words = {}  # 存储分词结果
        self.neighbor = {}  # 存储出现的左右临近字
        self.all_word_count = 0  # 全部词语数量数
        self.prat_1_len = 0
        self.prat_2_len = 0
        self.prat_3_len = 0
        self.result_data = None

    def run(self) -> None:
        try:
            prat_1_len = self.args.data.shape[0]
            do = 0
            for i, doc in enumerate(self.args.data[self.args.input_column].values):
                self.get_words(doc)
                if do != int((i + 1) / prat_1_len * 30):
                    do = int((i + 1) / prat_1_len * 30)
                    self.barSignal.emit(do)
            prat_2_len = len(self.words.items())
            for i, (k, v) in enumerate(self.words.items()):
                freq = self.words[k]['Count'] / self.all_word_count
                v['Freq'] = freq
                v['H'] = -np.log10(freq)
                if do != int((i + 1) / prat_2_len * 20) + 30:
                    do = int((i + 1) / prat_2_len * 20) + 30
                    self.barSignal.emit(do)
            prat_3_len = len(self.words.items())
            for i, (k, v) in enumerate(self.words.items()):
                if len(k) == 1:
                    self.words[k]['Dop'] = 0
                else:
                    dop = np.array(
                        [self.words[k[0:i]]['Freq'] * self.words[k[i:len(k)]]['Freq'] for i in range(1, len(k))]).sum()
                    v['Dop'] = np.log10(v['Freq'] / dop)
                left_words = self.neighbor[k]['LeftWords']
                right_words = self.neighbor[k]['RightWords']
                len_left_list = len(left_words)
                left_item = Counter(left_words)
                len_right_list = len(right_words)
                right_item = Counter(right_words)
                left = 0
                right = 0
                for _, l_v in left_item.items():
                    left += abs((l_v / len_left_list) * np.log10(1 / len(left_item)))
                for _, r_v in right_item.items():
                    right += abs((r_v / len_right_list) * np.log10(1 / len(right_item)))
                v['RightFree'] = right
                v['LeftFree'] = left
                v['Sum'] = v['H'] * self.args.H + \
                           v['Dop'] * self.args.Dop + \
                           v['LeftFree'] * self.args.LeftFree + \
                           v['RightFree'] * self.args.RightFree
                if do != int((i + 1) / prat_3_len * 40) + 50:
                    do = int((i + 1) / prat_3_len * 40) + 50
                    self.barSignal.emit(do)

            self.result_data = pd.DataFrame(self.words).T.sort_values('Sum', ascending=False)
            self.barSignal.emit(91)
            self.result_data = self.result_data.reset_index()
            self.barSignal.emit(92)
            self.result_data.columns = ['Word'] + list(self.result_data.columns)[1:]
            self.barSignal.emit(93)
            self.result_data = self.result_data.loc[(self.result_data.Dop > 0) | (
                    (self.result_data.RightFree > 0.0001) &
                    (self.result_data.LeftFree > 0.0001) &
                    (self.result_data.Freq > 0.0001) &
                    (self.result_data.Len > 1)
            )]
            self.barSignal.emit(94)
            self.result_data.H = round(self.result_data.H, 4)
            self.barSignal.emit(95)
            self.result_data.Dop = round(self.result_data.H, 4)
            self.barSignal.emit(96)
            self.result_data.RightFree = round(self.result_data.RightFree, 4)
            self.barSignal.emit(97)
            self.result_data.LeftFree = round(self.result_data.LeftFree, 4)
            self.barSignal.emit(98)
            self.result_data.Freq = round(self.result_data.Freq, 4)
            self.barSignal.emit(99)
            self.result_data.Sum = round(self.result_data.Sum, 4)
            self.barSignal.emit(100)
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())

    def get_words(self, doc) -> None:
        '''
        用来从文本中分词

        :param doc:  str 文本
        :return:
        '''
        doc = str(doc).strip()
        docs = re.findall(pattern='[\u4e00-\u9fa5]+', string=doc)
        for doc in docs:
            doc_len = len(doc)
            for word_index in range(doc_len):
                for i in range(1, self.args.parma):
                    if word_index + i + 1 <= doc_len:
                        split_word = doc[word_index:word_index + i]
                        left_word = doc[word_index - 1:word_index].strip()
                        right_word = doc[word_index + i:word_index + i + 1].strip()
                        if self.words.get(split_word, None) is None:
                            self.all_word_count += 1
                            self.words[split_word] = {'Count': 1, 'Len': len(split_word.strip())}
                            self.neighbor[split_word] = {'LeftWords': [left_word], 'RightWords': [right_word]}
                        else:
                            self.all_word_count += 1
                            self.words[split_word]['Count'] = self.words[split_word]['Count'] + 1
                            self.neighbor[split_word]['LeftWords'].append(left_word)
                            self.neighbor[split_word]['RightWords'].append(right_word)


# 文本分词线程
class CutWordThread(QThread):
    barSignal = Signal(int)
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, args):
        super(CutWordThread, self).__init__()
        self.args = args
        self.re_userdict = re.compile('^(.+?)( [0-9]+)?( [a-z]+)?$', re.U)

    def run(self) -> None:
        try:
            importlib.reload(jieba)
            importlib.reload(posseg)
            importlib.reload(analyse)
            words_count_dict = {}
            result = []
            func_dict = {
                '精确模式': lambda x: jieba.lcut(x),
                '全模式': lambda x: jieba.lcut(x, cut_all=True),
                '搜索引擎模式': lambda x: jieba.lcut_for_search(x),
                '关键词抽取模式 (TextRank)': lambda x: analyse.textrank(x, topK=self.args.extraction, allowPOS=self.args.pos),
                '关键词抽取模式 (TF-IDF)': lambda x: analyse.extract_tags(x, topK=self.args.extraction, allowPOS=self.args.pos)
            }
            l = len(self.args.user_word)
            bar = 0
            for i, line in enumerate(self.args.user_word):
                word, freq, tag = self.re_userdict.match(line).groups()
                if freq is not None:
                    freq = freq.strip()
                if tag is not None:
                    tag = tag.strip()
                jieba.add_word(word, freq, tag)
                if int((i + 1) / l * 5) != bar:
                    bar = int(i / l * 5)
                    self.barSignal.emit(bar + 1)
            l = self.args.data.shape[0]
            bar = 0
            # if self.args.model_select in ['精确模式', '全模式', '搜索引擎模式','关键词抽取模式 (TextRank)','关键词抽取模式 (TF-IDF)']:
            if self.args.model_select == '词性筛选模式':
                for i, row in enumerate(self.args.data[self.args.input_column].values):
                    text = str(row)
                    words = []
                    for word, pos in posseg.cut(text):
                        if word not in self.args.stop_word and pos in self.args.pos:
                            words.append(word)
                            words_count_dict[word] = words_count_dict.get(word, 0) + 1
                    result.append(' '.join(words))
                    if int((i + 1) / l * 90) != bar:
                        bar = int((i + 1) / l * 90)
                        self.barSignal.emit(bar + 6)
            else:
                func = func_dict[self.args.model_select]
                for i, row in enumerate(self.args.data[self.args.input_column].values):
                    text = str(row)
                    words = []
                    for word in func(text):
                        if word not in self.args.stop_word:
                            words.append(word)
                            words_count_dict[word] = words_count_dict.get(word, 0) + 1
                    result.append(' '.join(words))
                    if int((i + 1) / l * 90) != bar:
                        bar = int(i / l * 90)
                        self.barSignal.emit(bar + 6)

            self.args.word_count_data = pd.DataFrame([words_count_dict]).T.reset_index().rename(
                columns={'index': '词', 0: '词频'}).sort_values('词频', ascending=False).reset_index(drop=True)
            self.barSignal.emit(98)
            self.args.data[f'分词结果_{self.args.model_select}'] = result
            self.barSignal.emit(100)
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())


# 文本聚类线程
class TextClusteringThread(QThread):
    barSignal = Signal(int)
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, args):
        super(TextClusteringThread, self).__init__()
        self.args = args
        if not jpype.isJVMStarted():
            try:
                jvm_path = jpype.getDefaultJVMPath() if config.get('JVM', 'jvm_path') == '' else config.get('JAR',
                                                                                                            'JVM_Path')
                jars = os.pathsep.join([i for _, i in config.items('JAR')])
                jvm_xms = config.get('JVM', 'jvm_xms')
                jvm_xmx = config.get('JVM', 'jvm_xmx')
                start_jvm(jvm_path=jvm_path, jars=jars, jvm_xms=jvm_xms, jvm_xmx=jvm_xmx)
                self.JVM_error = None
            except:
                self.JVM_error = traceback.format_exc()
                # jpype.shutdownJVM()
        self.JVM_status = jpype.isJVMStarted()

    def run(self) -> None:
        try:
            from javaClass import ClusterAnalyzer
            analyzer = ClusterAnalyzer()
            lens = self.args.data.shape[0]
            step = 0
            for i, text in enumerate(self.args.data[self.args.input_column].values):
                if int((i + 1) / lens * 50) == step:
                    self.barSignal.emit(step + 1)
                    step += 1
                analyzer.addDocument(i, str(text))
            self.barSignal.emit(50)
            if self.args.select_model == 'K 均值聚类-自定类目数量':
                res = analyzer.kmeans(self.args.parma)
            else:
                res = analyzer.repeatedBisection(self.args.parma)
            self.barSignal.emit(70)
            id2class = {Id: i for (i, Ids) in enumerate(res) for Id in Ids}
            self.barSignal.emit(90)
            class_ids = pd.DataFrame([id2class]).T.sort_index()
            class_ids.columns = [f"{self.args.select_model}_{self.args.parma}_Class_Ids"]
            self.args.data = pd.concat([self.args.data, class_ids], axis=1)
            self.barSignal.emit(100)
            self.endSignal.emit()
        except:
            self.errorSignal.emit(traceback.format_exc())


# 词云图制作线程
class MakeWordCloudThread(QThread):
    barSignal = Signal(int)
    errorSignal = Signal(str)
    endSignal = Signal()

    def __init__(self, args):
        super(MakeWordCloudThread, self).__init__()
        self.args = args
        self.wc = None
        self.img = None

    def run(self) -> None:
        try:
            if self.args.FontModel[1]:
                word_color = lambda *args, **kwargs: self.args.font_colour[0]
            else:
                word_color = None
            if self.args.background_mask:
                img = Image.open(self.args.background_img_path)
                mask = np.array(img)
            else:
                mask = None
            self.wc = wordcloud.WordCloud(font_path=self.args.font_file_path,
                                          width=self.args.width,
                                          height=self.args.height,
                                          margin=self.args.margin,
                                          prefer_horizontal=self.args.prefer_horizontal,
                                          mask=mask,
                                          color_func=word_color,
                                          max_words=self.args.max_word,
                                          background_color=None if self.args.no_background else
                                          self.args.background_colour[0],
                                          relative_scaling=self.args.relative_scaling,
                                          mode='RGBA' if self.args.no_background else 'RGB',
                                          scale=config.getint('WordCloudModel', 'scale'),
                                          min_font_size=config.getint('WordCloudModel', 'min_font_size'),
                                          max_font_size=None if config.get('WordCloudModel',
                                                                           'max_font_size') == 'null' else int(
                                              config.get('WordCloudModel', 'max_font_size'))
                                          )
            self.wc.generate_from_frequencies(self.args.data)
            if self.args.FontModel[2] and self.args.font_colour_dict is not None:
                recolor_func = GroupedColorFunc(self.args.font_colour_dict, '#FFFFFF')
                self.wc.recolor(color_func=recolor_func)
            self.img = Image.fromarray(np.uint8(self.wc.to_array()))
            self.endSignal.emit()
        except:
            traceback.print_exc()
            self.errorSignal.emit(traceback.format_exc())
        # self.wc.to_file("alice.png")

# -*- coding: utf-8 -*-
# @Time     : 2022/1/22 10:13 AM
# @File     : utils.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 工具类

__all__ = ['Args', 'GroupedColorFunc', 'config', 'start_jvm', 'default_stopword', 'built_version', 'built_date']

import os
import jpype
import configparser
from pandas import DataFrame
from wordcloud import get_single_color_func

built_version = '0.0.2'
built_date = 'February 10, 2022'

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src', 'config.ini'), encoding='utf-8')

try:
    if config.getint('Preference', 'work_space') == 0:
        config.set('Preference', 'work_space_path', os.path.join(os.path.expanduser('~'), "Desktop"))
    elif config.getint('Preference', 'work_space') == 1:
        config.set('Preference', 'work_space_path', os.path.join(os.path.expanduser('~'), "Document"))
    else:
        config.set('Preference', 'work_space_path', os.path.dirname(os.path.realpath(__file__)))
except:
    config.set('Preference', 'work_space', '2')
    config.set('Preference', 'work_space_path', os.path.dirname(os.path.realpath(__file__)))


class Args(object):
    def __init__(self, name):
        self.args_name = name

    def __str__(self):
        return_str = 'Args(\n'
        for attribute in dir(self):
            if '__' not in str(attribute):
                item = getattr(self, attribute)
                if type(item) == DataFrame:
                    return_str += f"\t{attribute} = DataFrame(\n\t\tshape = {item.shape}\n\t\tcolumn = {item.columns.tolist()}\n\t)\n"
                elif type(item) == str:
                    return_str += f"\t{attribute} = '{item}'\n"
                else:
                    return_str += f"\t{attribute} = {item}\n"
        return return_str + ')'


class GroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func
        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)


def start_jvm(jvm_path, jars, jvm_xms, jvm_xmx):
    JAVA_JAR_CLASSPATH = "-Djava.class.path=" + jars
    jpype.startJVM(jvm_path, "-ea", JAVA_JAR_CLASSPATH, "-Xms%s" % jvm_xms, "-Xmx%s" % jvm_xmx, convertStrings=True)


with open('./src/default_stopword.txt', encoding='utf-8') as f:
    default_stopword = [i.strip('\n') for i in f.readlines()]

if __name__ == '__main__':
    pass

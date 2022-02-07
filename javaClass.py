# -*- coding: utf-8 -*-
# @Time     : 2022/1/25 13:48
# @File     : javaClass.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : Java类

__all__ = ['ClusterAnalyzer', 'HanLP']

import jpype


# def normalizing(address: str):
#     """
#     地址标准化
#     :param address: 文本地址
#     :return:
#     """
#     geocoding = jpype.JClass('io.patamon.geocoding.Geocoding')
#     address_nor_java = geocoding.normalizing(str(address))
#     pattern = re.compile(
#         "Address\(\n\tprovinceId=(.*?), province=(.*?), " +
#         "\n\tcityId=(.*?), city=(.*?), " +
#         "\n\tdistrictId=(.*?), district=(.*?), " +
#         "\n\tstreetId=(.*?), street=(.*?), " +
#         "\n\ttownId=(.*?), town=(.*?), " +
#         "\n\tvillageId=(.*?), village=(.*?), " +
#         "\n\troad=(.*?), " +
#         "\n\troadNum=(.*?), " +
#         "\n\tbuildingNum=(.*?), " +
#         "\n\ttext=(.*?)\n\)"
#         , re.S)
#     try:
#         info = re.findall(pattern, str(address_nor_java.toString()))[0]
#         info = [None if i == 'null' or i == 'nan' else i for i in info]
#         return Address(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9],
#                        info[10], info[11], info[12], info[13], info[14], info[15], address_nor_java)
#     except AttributeError:
#         return Address
#
#
# class Address(object):
#     def __init__(self, provinceId=None, province=None, cityId=None, city=None, districtId=None, district=None,
#                  streetId=None, street=None, townId=None, town=None, villageId=None, village=None, road=None,
#                  roadNum=None, buildingNum=None, text=None, java=None):
#         self.provinceId = int(provinceId) if provinceId else provinceId
#         self.province = province
#         self.cityId = int(cityId) if cityId else cityId
#         self.city = city
#         self.districtId = int(districtId) if districtId else districtId
#         self.district = district
#         self.streetId = int(streetId) if streetId else streetId
#         self.street = street
#         self.townId = townId
#         self.town = town
#         self.villageId = villageId if villageId is not None else None
#         self.village = village
#         self.road = road
#         self.roadNum = roadNum
#         self.buildingNum = buildingNum
#         self.text = text
#         self._AddressClass = jpype.JClass('io.patamon.geocoding.model.Address')
#         self._java = java if java is not None else self._AddressClass(self.provinceId, self.province, self.cityId,
#                                                                       self.city, self.districtId, self.district,
#                                                                       self.streetId, self.street, self.townId,
#                                                                       self.town,
#                                                                       self.villageId, self.village, self.road,
#                                                                       self.roadNum, self.buildingNum, self.text)
#
#     def __str__(self):
#         return (f"Address(\n\tprovinceId={self.provinceId}, province={self.province}, " +
#                 f"\n\tcityId={self.cityId}, city={self.city}, " +
#                 f"\n\tdistrictId={self.districtId}, district={self.district}, " +
#                 f"\n\tstreetId={self.streetId}, street={self.street}, " +
#                 f"\n\ttownId={self.townId}, town={self.town}, " +
#                 f"\n\tvillageId={self.villageId}, village={self.village}, " +
#                 f"\n\troad={self.road}, " +
#                 f"\n\troadNum={self.roadNum}, " +
#                 f"\n\tbuildingNum={self.buildingNum}, " +
#                 f"\n\ttext={self.text}\n)")
#
#     @property
#     def __dict__(self):
#         return {
#             'provinceId': self.provinceId,
#             'province': self.province,
#             'cityId': self.cityId,
#             'city': self.city,
#             'districtId': self.districtId,
#             'district': self.district,
#             'streetId': self.streetId,
#             'street': self.street,
#             'townId': self.townId,
#             'town': self.town,
#             'villageId': self.villageId,
#             'village': self.village,
#             'road': self.road,
#             'roadNum': self.roadNum,
#             'buildingNum': self.buildingNum,
#             'text': self.text
#         }
#
#
# class RegionTypes(object):
#     RegionTypeClass = jpype.JClass('io.patamon.geocoding.model.RegionType')
#     Undefined = RegionTypeClass.Undefined  # 未定义区域类型
#     Country = RegionTypeClass.Country  # 国家
#     Province = RegionTypeClass.Province  # 省份
#     ProvinceLevelCity1 = RegionTypeClass.ProvinceLevelCity1  # 直辖市 - 与省份并行的一级
#     ProvinceLevelCity2 = RegionTypeClass.ProvinceLevelCity2  # 直辖市 - 与城市并行的一级
#     City = RegionTypeClass.City  # 地级市
#     CityLevelDistrict = RegionTypeClass.CityLevelDistrict  # 省直辖县级市
#     District = RegionTypeClass.District  # 县、区
#     Street = RegionTypeClass.Street  # 街道乡镇一级
#     PlatformL4 = RegionTypeClass.PlatformL4  # 特定平台的4级地址
#     Town = RegionTypeClass.Town  # 附加：乡镇
#     Village = RegionTypeClass.Village  # 附加：村
#
#
# def addRegionEntry(Id: int, parentId: int, name: str, region_type: RegionTypes, alias=''):
#     """
#     添加自定义地址信息
#     :param Id: 地址的ID
#     :param parentId: 地址的父ID, 必须存在
#     :param name: 地址的名称
#     :param region_type: 地址类型,RegionType,
#     :param alias: 地址的别名, default=''
#     :return:
#     """
#     geocoding = jpype.JClass('io.patamon.geocoding.Geocoding')
#     try:
#         geocoding.addRegionEntry(Id, parentId, name, region_type, alias)
#         return True
#     except:
#         return False
#

def _attach_jvm_to_thread():
    """
    use attachThreadToJVM to fix multi-thread issues: https://github.com/hankcs/pyhanlp/issues/7
    """
    if not jpype.isThreadAttachedToJVM():
        jpype.attachThreadToJVM()


class SafeJClass(object):
    def __init__(self, proxy):
        """
        JClass的线程安全版
        :param proxy: Java类的完整路径，或者一个Java对象
        """
        self._proxy = jpype.JClass(proxy) if type(proxy) is str else proxy

    def __getattr__(self, attr):
        _attach_jvm_to_thread()
        return getattr(self._proxy, attr)

    def __call__(self, *args):
        if args:
            proxy = self._proxy(*args)
        else:
            proxy = self._proxy()
        return SafeJClass(proxy)


class LazyLoadingJClass(object):
    def __init__(self, proxy):
        """
        惰性加载Class。仅在实际发生调用时才触发加载，适用于包含资源文件的静态class
        :param proxy:
        """
        self._proxy = proxy

    def __getattr__(self, attr):
        _attach_jvm_to_thread()
        self._lazy_load_jclass()
        return getattr(self._proxy, attr)

    def _lazy_load_jclass(self):
        if type(self._proxy) is str:
            self._proxy = jpype.JClass(self._proxy)

    def __call__(self, *args):
        self._lazy_load_jclass()
        if args:
            proxy = self._proxy(*args)
        else:
            proxy = self._proxy()
        return SafeJClass(proxy)


CustomDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CustomDictionary')
HanLP = SafeJClass('com.hankcs.hanlp.HanLP')
HanLP.Config = jpype.JClass('com.hankcs.hanlp.HanLP$Config')
ClusterAnalyzer = jpype.JClass('com.hankcs.hanlp.mining.cluster.ClusterAnalyzer')

if __name__ == '__main__':
    # text = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    # res = normalizing(text)
    # print(res)
    # addRegionEntry(1, 321200000000, "A街道", RegionTypes.Street)
    # test_address = normalizing("江苏泰州A街道")
    # print(test_address)
    # hanlp = HanLP(
    #     jvm_path=os.path.join(_src_path, 'src/TencentKona/bin/server/jvm.dll'),
    #     jar_class_path=os.path.join(_src_path, 'src/Hanlp/hanlp-1.8.2.jar'),
    #     data_path=os.path.join(_src_path, 'src/Hanlp'),
    # )
    pass

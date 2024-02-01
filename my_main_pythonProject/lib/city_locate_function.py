#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""城市定位相关功能接口"""

import math

import requests
from loguru import logger

from lib.common_function import config, ini_path
from lib.requests_function.requests_server import get_city_locate_data
from lib.wifi_function import WifiFunction


def get_city_locate():
    wifi = WifiFunction()
    res, ip_address = wifi.is_ipv6_or_ipv4()
    data = get_city_locate_data(ip_address=ip_address).get("request")
    # {'province': '安徽省', 'city': '合肥市', 'district': '长丰', 'isp': '电信'}
    province = data.get('province')
    city = data.get('city')
    district = data.get('district')
    isp = data.get('isp')
    # 存入本地
    wtite_to_config(province, city, district, isp)
    logger.debug(f'{province}, {city}, {district},{isp}')


def get_longitude_and_latitude(ip):
    # 接口地址
    url = "https://api.map.baidu.com/location/ip"
    # 此处填写你在控制台-应用管理-创建应用后获取的AK
    ak = "jpkNxXsisBbZlQH6t8PONa1LOVUrjCYd"
    params = {
        "ip": ip,
        "coor": "bd09ll",
        "ak": ak,

    }

    response = requests.get(url=url, params=params)
    if response:
        address = response.json().get('content').get('address')
        point = response.json().get('content').get('point')
        longitude = point.get('x')
        latitude = point.get('y')
        logger.debug(f"定位:{address},经度:{longitude},纬度:{latitude}")
        return address, longitude, latitude


def haversine_distance(lat1, lon1, lat2, lon2):
    # 将经纬度转换为弧度
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # 应用 haversine 公式计算距离
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # 地球半径为 6371 公里

    return distance


def wtite_to_config(province, city, district, isp):
    # 将用户名和密码写入配置文件
    config.set('address', 'province', province)
    config.set('address', 'city', city)
    config.set('address', 'district', district)
    config.set('address', 'isp', isp)
    # 将配置信息写入本地文件
    with open(ini_path, 'w') as f:
        config.write(f)

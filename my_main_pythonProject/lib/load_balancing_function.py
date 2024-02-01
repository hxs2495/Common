# -*- coding: utf-8 -*-
"""
负载均衡功能接口
"""
import random
import subprocess
import time

import requests
from loguru import logger

from lib.common_function import config, ini_path
from lib.requests_function.requests_server import get_load_balancing

city_address = config.get('address', 'city')


# 获取就近服务器地址
def load_balancing():
    # data = {'method': 'get_data', 'sql': f"select * from server_ip where city_address='{city_address}';"}
    result = get_load_balancing().get("request")
    id = test_ping_server_ip(result)
    desired_dict = None
    for item in result:
        if item['id'] == id:
            desired_dict = item
            break
    write_to_conf(desired_dict)
    return desired_dict


def write_to_conf(result):
    # # 将数据存储到conf.ini文件中
    section_name = "server_ip"
    if section_name not in config.sections():
        config.add_section(section_name)
    for key, value in result.items():
        config.set(section_name, key, str(value))
    # 将配置写入conf.ini文件
    with open(ini_path, 'w') as configfile:
        config.write(configfile)


# 根据获取到的多个server_ip集合进行网络测速，择优返回server_ip
def test_ping_server_ip(server_ip_list):
    fastest_ip = None
    fastest_id = None
    min_speed = float('inf')  # 初始化为正无穷大的延迟时间
    # 测试每个server_ping_ip的通信速度并找到最快的
    for item in server_ip_list:
        id = item['id']
        server_ip = item['server_ping_ip']
        ping_speed = test_ping_speed(server_ip)
        logger.debug(f'正在ping服务地址{server_ip},测得响应速度为{ping_speed}毫秒')

        if ping_speed is not None and ping_speed < min_speed:
            min_speed = ping_speed
            fastest_ip = server_ip
            fastest_id = id
    if fastest_ip is not None:
        logger.debug(f'速度最快的server_ping_ip是：{fastest_ip},id索引为{fastest_id}')
        return fastest_id
    else:
        logger.debug('无法连接到任何服务器,连接中间服务器获取最新配置')
        wait_time = random.uniform(0, 3)  # 随机生成一个0~3之间的浮点数作为等待时间
        time.sleep(wait_time)  # 等待一段随机时间
        # get_server_new_config()  # 调用连接中间服务器获取最新配置函数



# 测速函数
def test_ping_speed(server_ip):
    try:
        # 执行ping命令并捕获输出
        output = subprocess.check_output(['ping', '-c', '10', server_ip])
        output = output.decode('utf-8')  # 将字节转换为字符串
        # 提取平均延迟时间
        lines = output.split('\n')
        for line in lines:
            if 'rtt min/avg/max/mdev' in line:
                avg_time = line.split('=')[1].split('/')[1]
                return float(avg_time)
    except subprocess.CalledProcessError:
        pass
    return None


# 处理无法直接连接服务器，从而连接中间服务器获取服务最新配置
def get_server_new_config():
    API_KEY = 'ab9bdf5301e618482fe1746e25b589fc'
    url = 'http://127.0.0.1:8000/get_server_new_config/'
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'city_address': city_address
    }
    try:
        # 发送POST请求
        response = requests.post(url, data=data)
    except:
        pass
    else:
        # 解析响应数据
        json_data = response.json()
        # 输出响应结果
        print(json_data)
        write_to_conf(json_data.get("request"))



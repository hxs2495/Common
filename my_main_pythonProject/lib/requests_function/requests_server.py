#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
数据接受发送功能接口
"""
import datetime
import os.path

import requests

from conf import setting
from lib.machine_systems.get_sip_cpuid import get_sip, get_cpuid

API_KEY = setting.API_KEY
redis_host = setting.redis_url
icare_host = setting.icare_url
cloud_host = setting.cloud_url


def send_request(url, data):
    try:
        # 发送POST请求
        response = requests.post(url=url, data=data)
    except:
        print("请求服务端异常")
        return None
    print(response)
    # 解析响应数据
    json_data = response.json()
    # 输出响应结果
    print(json_data)
    return json_data


def send_user_information(user_information):
    """向服务端发送用户数据"""
    address = "save/userinformation/"
    url = os.path.join(redis_host, address)

    data = user_information.copy()
    data.update({"api_key": API_KEY})

    return send_request(url, data)


def get_server_count():
    """获取服务额度"""
    address = "get/server/count/"
    url = os.path.join(redis_host, address)

    data = {"api_key": API_KEY, "sip": get_sip()}

    return send_request(url, data)


def get_cloud_apikey():
    """获取云服务读参系统API_KEY"""
    address = "get/apikey/"
    url = os.path.join(redis_host, address)

    data = {"api_key": API_KEY, "sip": get_sip()}

    return send_request(url, data)


def update_server_count(server_count):
    """更新服务额度"""
    address = "update/server/count/"
    url = os.path.join(redis_host, address)

    data = {"api_key": API_KEY, "sip": get_sip(), "server_count": server_count}

    return send_request(url, data)


def upload_file(file_path):
    """向服务端上传文件"""
    # 替换为实际的后端上传接口URL
    address = "upload/file/"
    url = os.path.join(redis_host, address)
    data = {"api_key": API_KEY, "sip": get_sip()}

    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        print('文件上传成功！')
    else:
        print('文件上传失败。')


def download_file(file_name, save_directory=""):
    """向服务端请求下载指定文件"""
    address = "download/file/"
    url = os.path.join(redis_host, address)
    # 文件保存路径
    save_path = os.path.join(save_directory, file_name)

    params = {'file_name': file_name}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
            print("文件下载成功")
            return True
    else:
        print("文件下载失败")
        return False


def send_feedback_information(feedback_phone, feedback_suggestion):
    """向服务端发送用户反馈数据"""
    data = {
        "api_key": API_KEY,
        "sip": get_sip(),
        "feedback_phone": feedback_phone,
        "feedback_type": "机器端反馈",
        "feedback_suggestion": feedback_suggestion
    }
    address = "save/feedback/information/"
    url = os.path.join(redis_host, address)

    return send_request(url, data)


def update_call_minute(call_minute):
    """更新服务额度"""
    address = "update/call/minute/"
    url = os.path.join(redis_host, address)

    data = {"api_key": API_KEY, "sip": get_sip(), "call_minute": call_minute}

    return send_request(url, data)


def get_load_balancing():
    """获取就近服务地址额度"""
    address = "get/load/balancing/"
    url = os.path.join(redis_host, address)

    data = {"api_key": API_KEY, "city_address": "合肥市"}

    return send_request(url, data)


def get_server_latest_config():
    """获取中间服务器最新服务地址"""
    address = 'get/server/latest/config/'
    url = os.path.join(redis_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'city_address': "合肥市"
    }
    return send_request(url, data)


def get_city_locate_data(ip_address):
    """获取城市定位数据"""
    address = 'get/city/locate/'
    url = os.path.join(redis_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'ip_address': ip_address
    }
    return send_request(url, data)


def get_version_number():
    """获取程序最新版本数据"""
    address = 'get/version/number/'
    url = os.path.join(redis_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'sip': get_sip(),
    }
    return send_request(url, data)


def get_random_chat_user(gender, age_start, age_end):
    """获取随机聊天用户"""
    address = 'get/random/chat/user/'
    url = os.path.join(redis_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'sip': get_sip(),
        'gender': gender,
        'age_start': age_start,
        'age_end': age_end,
    }
    return send_request(url, data)


def get_intelligent_customer_service(issue):
    """获取智能客服答复"""
    address = 'get/intelligent/customer/service/'
    url = os.path.join(redis_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'issue': issue,
    }
    return send_request(url, data)


def save_machine_reports(sip, cpuid, report, electricity):
    """发送保存机器报告数据"""
    address = 'save/machine/reports/'
    url = os.path.join(icare_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'sip': sip,
        'cpuid': cpuid,
        'electricity': electricity,
        'report': report,
    }
    return send_request(url, data)


def get_servertime():
    """获取机器人服务在线和离线时长"""
    address = 'get/servertime/'
    url = os.path.join(icare_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'sip': get_sip(),
        'cpuid': get_cpuid(),
        'ctime': datetime.datetime.now(),
    }
    return send_request(url, data)


def get_user_isbusy(target_sip):
    address = 'get/user/isbusy/'
    url = os.path.join(redis_host, address)
    # 构造请求参数
    data = {
        'api_key': API_KEY,
        'sip': get_sip(),
        'target_sip': target_sip,
    }
    return send_request(url, data)


if __name__ == '__main__':
    pass

    # user_information = execute_sql(sql='SELECT * FROM user_information limit 1')[0]
    # print(user_information)
    # user_information_test = {
    #     "name": "小白",
    #     "nickname": "小白小帅",
    #     "sex": "男",
    #     "age": 28,
    #     "phone": "13800138000",
    #     "identity_card": "110101199001010001",
    #     "address": "北京市朝阳区",
    #     "height": "175cm",
    #     "weight": "70kg",
    #     "marriage": "未婚",
    #     "basic_disease": "无",
    #     "user_note": "这是一条测试记录",
    #
    #     "linkpeople1_name": "李四",
    #     "linkpeople1_relationship": "朋友",
    #     "linkpeople1_phone": "13900139001",
    #     "linkpeople1_note": "这是一条测试记录中的联系人1",
    #
    #     "linkpeople2_name": "王五",
    #     "linkpeople2_relationship": "同事",
    #     "linkpeople2_phone": "13900139002",
    #     "linkpeople2_note": "这是一条测试记录中的联系人2",
    #
    #     "linkpeople3_name": None,
    #     "linkpeople3_relationship": None,
    #     "linkpeople3_phone": None,
    #     "linkpeople3_note": None,
    #
    #     "linkpeople4_name": None,
    #     "linkpeople4_relationship": None,
    #     "linkpeople4_phone": None,
    #     "linkpeople4_note": None,
    #
    #     "linkpeople5_name": None,
    #     "linkpeople5_relationship": None,
    #     "linkpeople5_phone": None,
    #     "linkpeople5_note": None,
    #
    #     "linkpeople6_name": None,
    #     "linkpeople6_relationship": None,
    #     "linkpeople6_phone": None,
    #     "linkpeople6_note": None,
    #
    #     "cpuid": "ABC123456789",
    #     "sip": get_sip(),
    #
    #     "init_time": None,
    #     "equipment_status": "使用中",
    #     "server_ip_id": 3,
    #     "customer_server_count": 3,
    #     "count_call_mintue": 300
    # }

    # 保存更新用户信息
    # send_user_information(user_information=user_information_test)

    # 获取服务额度
    # print(get_server_count().get("customer_server_count"))

    # 更新服务额度
    # update_server_count(server_count=-1)

    # 上传文件示例
    # file_path = '/home/hxs/PycharmProjects/new_maincontrol_plus/conf/setting.py'  # 替换为实际的文件路径
    # upload_file(file_path)
    # 下载文件示例
    # download_file(file_name="V23.002", save_directory="/home/hxs/PycharmProjects/new_maincontrol_plus")

    # 保存反馈信息
    # feedback_information = {
    #     "api_key": API_KEY,
    #     "sip": get_sip(),
    #     "feedback_phone": 17356677867,
    #     "feedback_type": "机器端反馈",
    #     "feedback_suggestion": "测试反馈建议"
    # }
    # send_feedback_information(feedback_information=feedback_information)

    # 更新通话时长额度
    # update_call_minute(call_minute=355)

    # print(get_load_balancing().get("request"))
    # get_server_latest_config()

    # wifi = WifiFunction()
    # res, ip_address = wifi.is_ipv6_or_ipv4()
    # print(res, ip_address)
    # ip_address = "36.5.4.103"
    # print(get_city_locate_data(ip_address=ip_address).get("request"))
    # print(get_version_number().get("request").get("new_version_number"))

    # get_servertime()

    # get_user_isbusy(target_sip=111114)

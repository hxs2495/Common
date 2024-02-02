#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

# 定义配置文件路径
BASE_PROJECT_DIR = os.getcwd()
ini_path = os.path.join(BASE_PROJECT_DIR, 'conf/conf.ini')

# 初始化界面模块参数配置
contact_relationship_list = ["儿子", "女儿", "孙子", "孙女", "其他"]
country_list = ["中国", "朝鲜", "韩国", "美国", "英国"]
language_list = ["中文简体", "中文繁体", "English", "日本語", "한국어"]
wifi_name_list = ['i-Care', 'TEI_915', 'VPU_519', 'YNU_927', 'GPJ_586', 'YTJ_886', 'AJE_065', 'SKE_850', 'AZU_726',
                  'BFV_628', 'FRB_053', 'IZR_104', 'QVA_116', 'EBS_839', 'ISY_468', 'IIN_765', 'AJL_468', 'OFB_119',
                  'QGB_266', 'NHW_687', 'QYP_479', 'HXN_277', 'BBL_631', 'AQE_872', 'OUZ_733', 'YPS_490', 'RAU_617',
                  'JQQ_434', 'TOX_626', 'TUA_192']

contacts_people_list = ['儿子', '女儿', '孙子', '李晓二', '张大仙', '小白', '小帅', '大儿媳', '外孙', '老刘', '老黄',
                        '小张', '小二', '小帅', '小锋', '小爱', '小园', ]

recent_contacts_list = ['老刘', '老黄', '小张', '小二', '儿子', '女儿', '孙子', '外孙']

test_wifi_name = "i-Care"
test_wifi_password = "iCareWillGreat!!!"

db_url = 'sqlite:///AppData/db/mydatabase.db'

user_agreement_path = "conf/static/docs/user_agreement.txt"
member_agreement_path = "conf/static/docs/member_agreement.txt"
announcements_path = "conf/static/docs/announcements.txt"
background_img = "conf/static/material/14.jpg"

# 主界面模块参数配置
# url
music_url = 'http://ainm.cc/music/'
video_url = 'https://libvio.top/type/1.html'
radio_url = 'http://www.guangbomi.com/'
smart_url = 'https://c2.binjie.fun/#/chat/1697700354508'

# server_url
ws_url = "ws://112.29.78.72:5004/ws/chat"
redis_url = "http://112.29.78.72:5006"
icare_url = "http://112.29.78.72:5004"
cloud_url = "http://127.0.0.1:8000"

API_KEY = 'ab9bdf5301e618482fe1746e25b589fc'

language_dict = {
    '中文简体': 'zh-CN',
    '中文繁体': 'zh-TW',
    'English': 'en',
    '日本語': 'ja',
    '한국어': 'ko',
}

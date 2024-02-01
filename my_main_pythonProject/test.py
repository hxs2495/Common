# -*- coding: utf-8 -*-
# 使用示例
import requests

from lib.requests_function.requests_server import get_city_locate_data
from lib.wifi_function import WifiFunction

# from lib.db_function import models
# from lib.db_function.db_interface import DatabaseManager
# from lib.db_function.models import Contact

# db_manager = DatabaseManager()
# db_manager.create_database()

# 添加一条联系人记录
# user_instance = Contact(
#     name='小黄', relationship='同学', contact_info='123456', sip_number='sip:123456', remark="hello"
# )
# db_manager.add_data(user_instance)


# # # 查询所有记录
# print(db_manager.get_data(table_class=Contact))
# # 查询指定记录
# record = db_manager.session.query(models.Contact.name, models.Contact.relationship).filter_by(id=4).first()
# print(record)

# # 修改信息
# # 查询要修改的记录
# record = db_manager.session.query(models.Contact).filter_by(id=4).first()
# # 修改记录的字段值
# record.name = "new"
# db_manager.update_data()

# 删除记录
# 查询要删除的记录
# record = db_manager.session.query(models.Contact).filter_by(id=3).first()
# db_manager.delete_data(record)


# //要查询的IP地址
IP = "39.156.69.79"
# //拼接url
url = f"http://api.vore.top/api/IPdata?ip={IP}"
# //请求数据并解码
result = requests.get(url)

# //输出IP归属地信息
print(result.json())
# {'code': 200, 'msg': 'SUCCESS', 'ipinfo': {'type': 'ipv6', 'text': 'fe80::e297:12b6:3514:4ee1', 'cnip': False}, 'ipdata': {'info1': '局域网', 'info2': '', 'info3': '', 'isp': ''}, 'adcode': {'o': '局域网 - ', 'p': '局域网', 'c': '局域网', 'n': '局域网-局域网', 'r': None, 'a': None, 'i': False}, 'tips': '接口由VORE-API(https://api.vore.top/)免费提供', 'time': 1706687373}

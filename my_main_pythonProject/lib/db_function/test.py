# -*- coding: utf-8 -*-
# 使用示例

# from lib.db_function import models
# from lib.db_function.db_interface import DatabaseManager
# from lib.db_function.models import Contact
#
# db_manager = DatabaseManager()
# db_manager.create_database()

# 添加一条联系人记录
# user_instance = Contact(
#     name='小黄', relationship='同学', contact_info='123456', sip_number='sip:123456', remark="hello"
# )
# db_manager.add_data(user_instance)


# # 查询所有记录
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

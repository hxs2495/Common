# -*- coding: utf-8 -*-
# database.py
import os

from loguru import logger
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session, class_mapper

from conf import setting
from lib.db_function.models import Base


class DatabaseManager:
    def __init__(self, db_url=setting.db_url):
        # 本地sqlite数据库连接地址
        self.db_url = db_url
        # 创建引擎
        self.engine = create_engine(self.db_url)
        # 绑定引擎
        self.Session = sessionmaker(bind=self.engine)
        # 内部会采用threading.local进行隔离
        self.session = scoped_session(self.Session)

    def create_database(self):
        if not os.path.exists(self.db_url):
            Base.metadata.create_all(self.engine)

            inspector = inspect(self.engine)
            existing_tables = inspector.get_table_names()

            for table in Base.metadata.tables.values():
                if table.name not in existing_tables:
                    table.create(self.engine)
        logger.debug("数据库初始化完成")

    def _commit_and_close(self):
        self.session.commit()
        self.session.close()

    def add_data(self, obj):
        self.session.add(obj)
        self._commit_and_close()

    def update_data(self):
        # self.session.merge(obj)
        self._commit_and_close()

    def delete_data(self, obj):
        self.session.delete(obj)
        self._commit_and_close()

    def get_data(self, table_class):
        mapper = class_mapper(table_class)

        columns = [column.key for column in mapper.columns]
        result = []
        for row in self.session.query(table_class).all():
            record_dict = {col: getattr(row, col) for col in columns}
            result.append(record_dict)
        self._commit_and_close()
        return result

# 使用示例

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

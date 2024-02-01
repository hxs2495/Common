# models.py
from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserInformation(Base):
    """ 用户信息表 """
    # 数据库中存储的表名
    __tablename__ = "user_information"
    # 对于必须插入的字段，采用nullable=False进行约束，它相当于NOT NULL
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, comment="姓名")
    # 对于非必须插入的字段，不用采取nullable=False进行约束
    nickname = Column(String(32), comment="昵称")
    sex = Column(String(32), default="男", comment="性别")
    age = Column(Integer, comment="年龄")
    phone = Column(String(32), comment="手机号")
    identity_card = Column(String(64), comment="身份证")
    address = Column(String(64), comment="地址")
    height = Column(String(64), comment="身高")
    weight = Column(String(64), comment="体重")
    marriage = Column(String(64), comment="婚姻状态")
    basic_disease = Column(String(64), comment="基础病")
    user_note = Column(String(64), comment="用户备注")

    user_state = Column(Integer, default=0, comment="用户状态，0表示正常，1表示弃用")


class ContactInformation(Base):
    __tablename__ = 'contacts_information'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), comment="联系人姓名")
    remark_name = Column(String(255), comment="别名")
    relationship = Column(String(50), comment="关系")
    contact_info = Column(String(100), comment="联系方式")
    sip_number = Column(String(20), comment="sip号")
    remark = Column(String(100), comment="备注")
    logotype = Column(Integer, default=0, comment="标识，0表示正常白名单，1表示已拉黑，2表示已删除，9表示紧急联系人")
    created_at = Column(String(255), default=datetime.now(), comment="创建时间")


class MachineInformation(Base):
    """机器信息"""
    __tablename__ = 'machine_information'
    id = Column(Integer, primary_key=True)
    cpuid = Column(String(64), nullable=False, comment="机器唯一CPU编码")
    sip = Column(String(64), nullable=False, comment="机器唯一SIP号")
    version_number = Column(Integer, default="23001", comment="机器软件版本号")
    language = Column(String(64), default="简体中文", comment="机器软件系统语言")
    equipment_status = Column(String(32), default="使用中", comment="机器人使用状态")
    init_time = Column(String(255), default=datetime.now, comment="创建时间")

    server_ip_id = Column(Integer, comment="通信服务地址")

    # 城市定位字段
    auto_locate_nation = Column(String(32), default="中国", comment="自动定位国家")
    auto_locate_province = Column(String(32), default="北京市", comment="自动定位省市")
    auto_locate_city = Column(String(32), default="北京市", comment="自动定位城市")
    auto_locate_district = Column(String(32), default="北京市", comment="自动定位区县")
    auto_locate_isp = Column(String(32), default="电信", comment="移动商")

    customer_server_count = Column(Integer, default=3, comment="用户会员服务剩余次数")
    count_call_mintue = Column(Integer, default=300, comment="外呼手机号码剩余费用")


class ChatRecords(Base):
    """ 聊天记录"""
    # 数据库中存储的表名
    __tablename__ = "chat_records"
    id = Column(Integer, primary_key=True)
    other_user_sip = Column(String(255), comment="其他用户sip号")
    other_user_name = Column(String(255), comment="其他用户姓名")
    user_sip = Column(String(255), comment="本人sip号")

    message = Column(String(255), comment="聊天信息")
    message_type = Column(Integer, comment="消息类型，区分文本、图片、文件等不同类型的消息")

    chat_sign = Column(String(255), comment="聊天标识")
    is_read = Column(Integer, default=1, comment="标识消息是否已读,0未读，1已读")
    create_time = Column(String(255), default=datetime.now, comment="聊天消息的时间戳，记录消息发送或接收的时间")


class TipsList(Base):
    """ 温馨提示词 """
    # 数据库中存储的表名
    __tablename__ = "tip_list"
    id = Column(Integer, primary_key=True)
    tips_text = Column(String(255), comment="温馨提示文本")
    tips_type = Column(Integer, default=0, comment="标识,用于区别不同类型提示")


class WifiList(Base):
    """ wifi密码 """
    # 数据库中存储的表名
    __tablename__ = "wifi_list"

    id = Column(Integer, primary_key=True)
    wifi_name = Column(String(255), comment="wifi名称")
    wifi_password = Column(String(255), comment="wifi密码")
    wifi_type = Column(Integer, default=0, comment="标识,用于区别不同类型")


class ServerList(Base):
    """ 服务地址 """
    # 数据库中存储的表名
    __tablename__ = "server_list"

    id = Column(Integer, primary_key=True)

    server_name = Column(String(255), comment="服务名称")
    server_address_ipv4 = Column(String(255), comment="服务ipv4地址")
    server_address_ipv6 = Column(String(255), comment="服务ipv6地址")
    server_port = Column(String(255), comment="服务端口")
    server_protocol = Column(String(255), comment="服务协议，如 HTTP、HTTPS、TCP、UDP")
    is_enabled = Column(Integer, default=0, comment="标识服务是否启用,0正常，1弃用")

    created_at = Column(String(255), default=datetime.now, comment="地址创建的时间戳，记录地址的创建时间")
    updated_at = Column(String(255), default=datetime.now, comment="地址更新的时间戳，记录地址的更新时间")

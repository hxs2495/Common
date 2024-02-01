#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""接收与APP端消息指令功能接口"""
import configparser
import socket

from PyQt5.QtCore import QThread, pyqtSignal
from loguru import logger

from db.db_handler import execute_sql
from lib.machine_systems.hardware_monitoring_function import get_sip


class ReceiveMessagesThread(QThread):
    receive_messages_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.client_b_socket = None
        self.connect_chat_server()
        # self.control = ConTrol()

    def connect_chat_server(self):
        if not self.client_b_socket or self.client_b_socket._closed:
            logger.debug('连接已关闭或未建立，开始连接')
            try:
                # 创建客户端B的套接字
                self.client_b_socket = socket.socket()
                # host = config.getstr('CHAT_SERVER_IP', 'host')
                # port = config.getint('CHAT_SERVER_IP', 'port')
                # 连接到服务器
                server_address = ('192.168.1.27', 5004)
                self.client_b_socket.connect(server_address)
                logger.debug('连接成功')
            except socket.timeout:
                # 连接超时处理逻辑
                logger.debug("连接超时")
            except socket.error as e:
                # 其他socket错误处理逻辑
                logger.debug(f"发生错误：, {str(e)}")
                return False
            else:
                # 发送客户端名称给服务器
                client_name = get_sip()
                self.client_b_socket.send(client_name.encode())
                return True
        else:
            logger.debug('连接已建立，无需再次连接')

    # 接收信息函数
    def run(self):
        while 1:
            logger.debug('启动消息接收循环监听')
            response = self.client_b_socket.recv(1024).decode()  # 接收服务器的响应
            logger.debug(response)
            command, target_client, content, other_user_sip = response.split('~&', 3)  # 根据特定格式解析响应内容
            print(command, target_client, content, other_user_sip)
            if command == 'SENDTO':  # 判断响应类型
                logger.debug('响应类型为控制信号')
                self.control_walking(content=content)
            elif command == 'MESSAGE':
                logger.debug('响应类型为聊天信号')
                # self.show_messages(content=content)
                self.receive_messages_result.emit(response)
            elif command == 'SETTING':
                logger.debug('响应类型为远程配置信号')
                print(command, target_client, content, other_user_sip)
                # send_file()
                self.send_confing_file(other_user_sip, target_client)
            else:
                # 接收到的响应类型无效，记录日志
                logger.debug(f'\n收到无效响应, {response}')

    # 如果接收到小车控制指令，则直接调用控制函数
    def control_walking(self, content):
        if '0' in content:
            logger.debug('APP端接管已断开，终止本次连接')
            # self.control.quit_control()
            return  # 若接收到的指令中包含'0'，表示APP端接管已断开，终止本次连接
        if 'z' in content:
            # 执行暂停操作
            logger.debug('执行暂停操作')
            # self.control.motor_stop()
        elif 'w' in content:
            logger.debug('执行前进操作')
            # self.control.motor_forward()
        elif 's' in content:
            # 执行后退操作
            logger.debug('执行后退操作')
            # self.control.motor_backward()
        elif 'a' in content:
            # 执行向左操作
            logger.debug('执行向左操作')
            # self.control.motor_left()
        elif 'd' in content:
            # 执行向右操作
            logger.debug('执行向右操作')
            # self.control.motor_right()

    def show_messages(self, content):
        pass

    def send_message(self, target_name, timestamp, target_sip, message, user_sip):
        # 保存聊天记录,0表示我发出的消息
        self.save_chat_message(target_sip, target_name, timestamp, message, user_sip, chat_sign=0)
        message = f'MESSAGE~&{target_sip}~&{message}~&{user_sip}'  # 构建消息内容，包括指令和目标客户端
        self.client_b_socket.send(message.encode())  # 将消息发送给服务端

    # 聊天记录存储函数
    def save_chat_message(self, other_user_sip, other_user_name, timestamp, message, user_sip, chat_sign):
        # chat_sign是0表示我方发出消息，1表示对方消息
        sql = "INSERT INTO chat_records (other_user_sip, other_user_name, timestamp, message, user_sip,chat_sign) VALUES (?,?,?,?,?,?)"
        parameters = (other_user_sip, other_user_name, timestamp, message, user_sip, chat_sign)
        execute_sql(sql, *parameters)
        logger.debug('聊天记录存入成功')

    def send_confing_file(self, target_sip, user_sip):
        FILE_PATH = "/home/hxs/PycharmProjects/new_maincontrol/conf/new_conf.ini"
        # filename = FILE_PATH.split('/')[-1]  # 提取文件名
        # self.client_b_socket.sendall(filename.encode())  # 发送文件名
        config = configparser.ConfigParser()
        config.read(FILE_PATH)

        data = {}
        for section in config.sections():
            data[section] = dict(config.items(section))

        message = f'SETTING~&{target_sip}~&{data}~&{user_sip}'  # 构建消息内容，包括指令和目标客户端
        # print(message)
        self.client_b_socket.send(message.encode())  # 将消息发送给服务端

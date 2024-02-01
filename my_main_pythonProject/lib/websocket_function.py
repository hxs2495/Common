import ast
import datetime
import os
import sys
import time

import requests
import websocket
from PyQt5.QtCore import QThread, pyqtSignal
from loguru import logger

from db.db_handler import execute_sql
# from lib.machine_systems.control_end import MotorController
from lib.requests_function.requests_server import upload_file


# 函数执行时间统计装饰器
def count_server_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        count_time = datetime.timedelta(seconds=end_time - start_time)
        time_str = str(count_time)
        logger.debug(f"本次服务总共用时:{time_str}")
        return result

    return wrapper


class WebSocketThread(QThread):
    message_received = pyqtSignal(str)
    request_received = pyqtSignal(str)
    schedule_received = pyqtSignal(dict)

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.request_handled = False
        # self.control = MotorController()

    def run(self):
        websocket.enableTrace(True)
        # 使用self.user_id在服务端建立群组

        url = f"ws://112.29.78.72:5004/ws/chat/{self.user_id}/"

        self.ws = websocket.WebSocketApp(url,
                                         on_open=self.on_open,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()

    def on_open(self, ws):
        """
        向服务端三次握手成功后建立连接，自动触发该方法
        :param ws:
        :return:
        """
        logger.debug("连接建立成功")

    def send_message(self, message, target_user_sip=1007, post_type='MESSAGE'):
        """
        向服务端发送数据
        :param message: 具体信息内容
        :param target_user_sip: 目标用户的sip号码
        :param post_type: 请求类型，SENDTO，MESSAGE，SETTING，LOGFILE，SCHEDULE
        :my_user_sip: 自身sip号码
        """
        data = {
            'type': post_type,
            'my_user_sip': self.user_id,
            'message': message,
            'target_user_sip': target_user_sip,
        }
        self.ws.send(str(data))

    def on_message(self, ws, rec_message):
        """
        接收服务端转发客户端发送的数据，并进行解析
        :param message:
        """
        logger.debug(rec_message)
        message_dict = ast.literal_eval(rec_message)
        data_type = message_dict.get("type")
        if data_type == "SENDTO":
            if message_dict.get("message") == "control":
                self.request_received.emit(message_dict.get("my_user_sip"))
                return

            logger.debug('响应类型为控制信号')
            self.control_walking(message_dict.get("message"))
        elif data_type == "MESSAGE":
            logger.debug('响应类型为聊天信号')
            self.message_received.emit(rec_message)
        elif data_type == "SETTING":
            logger.debug('响应类型为远程配置信号')
        elif data_type == "LOGFILE":
            logger.debug('响应类型为请求日志文件信号')
            self.send_logs()
        elif data_type == "SCHEDULE":
            logger.debug('响应类型为请求远程创建日程信号')
            # logger.debug(type(message_dict.get("message")), message_dict.get("message"))
            schedule_dict = self.str_to_dict(message_dict.get("message"))
            self.schedule_received.emit(schedule_dict)
        elif data_type == "SERVER_REBOOT":
            logger.debug('响应类型为请求后台远程重启服务')
            python = sys.executable  # 获取当前解释器的路径
            os.execl(python, python, *sys.argv)  # 通过新进程替代当前进程

    def on_error(self, ws, error):
        """接收服务端响应错误信息"""
        logger.debug('Error:', error)

    def on_close(self, ws):
        logger.debug('连接已关闭')
        # 连接异常断开，发送断开连接请求
        data = {
            'type': "disconnect",
            'my_user_sip': self.user_id,
            'message': "disconnect",
            'target_user_sip': None,
        }
        self.ws.send(str(data))

    # 如果接收到小车控制指令，则直接调用控制函数
    def control_walking(self, content):
        if '0' in content:
            logger.debug('APP端接管已断开，终止本次连接')
            # self.control.stop()
            return  # 若接收到的指令中包含'0'，表示APP端接管已断开，终止本次连接
        if 'z' in content:
            # 执行暂停操作
            logger.debug('执行暂停操作')
            # self.control.stop()
        elif 'w' in content:
            logger.debug('执行前进操作')
            # self.control.go_ahead()
        elif 's' in content:
            # 执行后退操作
            logger.debug('执行后退操作')
            # self.control.go_back()
        elif 'a' in content:
            # 执行向左操作
            logger.debug('执行向左操作')
            # self.control.turn_left()
        elif 'd' in content:
            # 执行向右操作
            logger.debug('执行向右操作')
            # self.control.turn_right()

    # 聊天记录存储函数
    def save_chat_message(self, other_user_sip, other_user_name, timestamp, message, user_sip, chat_sign):
        # chat_sign是0表示我方发出消息，1表示对方消息
        sql = "INSERT INTO chat_records (other_user_sip, other_user_name, timestamp, message, user_sip,chat_sign) VALUES (?,?,?,?,?,?)"
        parameters = (other_user_sip, other_user_name, timestamp, message, user_sip, chat_sign)
        execute_sql(sql, *parameters)
        logger.debug('聊天记录存入成功')

    @count_server_time
    def send_logs(self):
        file_path = f"logs/{datetime.date.today()}/{datetime.date.today()}.log"
        # 发送新增日志记录到Django服务端
        url = "http://112.29.78.72:5004/log_upload/"
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 读取新增的记录
            with open(file_path, 'r', encoding="utf-8") as file:
                log_content = file.read()
            # 构造请求参数
            data = {
                'api_key': 'ab9bdf5301e618482fe1746e25b589fc',
                'my_user_sip': self.user_id,
                'log_records': log_content,
                'day_date': datetime.date.today(),
            }
            response = requests.post(url, data=data)
            # 输出响应结果
            logger.debug(response.json())

    def upload_logs(self):
        file_path = f"logs/{datetime.date.today()}/{datetime.date.today()}.log"
        # 发送新增日志记录到Django服务端
        upload_file(file_path=file_path)

    def str_to_dict(self, raw_string):
        # 按逗号分割
        split_by_comma = raw_string.split(',')
        # 创建空字典
        result_dict = {}
        # # 根据冒号进行分割并添加到字典中
        for item in split_by_comma:
            key, value = item.split(':', 1)
            result_dict[key] = value

        sql = """INSERT INTO scheduled (scheduleid,time, context, sign) VALUES (?,?,?,?)"""
        parameters = (
            result_dict.get('scheduleid'), result_dict.get('time'), result_dict.get('content'),
            result_dict.get('repeat'))
        execute_sql(sql, *parameters)
        return result_dict

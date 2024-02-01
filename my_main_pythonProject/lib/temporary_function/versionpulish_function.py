# -*- coding: utf-8 -*-
"""主控版本更新功能接口"""
import datetime
import os
import socket

from PyQt5.QtCore import QThread
from loguru import logger

from db.db_handler import get_or_send_mysqldata
from lib.common_function import config, ini_path


class VersionPulishThread(QThread):
    def __init__(self):
        super().__init__()

    def detection_version_number(self):
        # 获取最新版本号与当前版本比对
        self.current_version_number = config.get('version', 'number')
        logger.debug(f'当前版本号：{self.current_version_number}')
        try:
            data = {'method': 'get_pulishdata', 'sql': "select version_num from pulishtable ORDER BY id desc LIMIT 1;"}
            self.new_version_number = get_or_send_mysqldata(data=data, method='get_data')[0].get('version_num')
            logger.debug(f'最新版本号：{self.new_version_number}')
        except:
            # 避免影响用户体验，那就设置最新版本就为当前版本，判断就提示当前已是最新版本
            self.new_version_number = self.current_version_number
        # 对比判断
        if self.current_version_number >= self.new_version_number:
            return False
        else:
            return self.new_version_number

    def update_now(self):
        # 获取连接参数
        host = config.get('UPDATE_SERVER_IP', 'host')  # 192.168.1.136 <class 'str'>
        port = config.getint('UPDATE_SERVER_IP', 'port')  # 5008 <class 'int'>
        # server_address = ('192.168.1.136', 5008)  # 替换为实际的服务器 IP 或主机名
        server_address = (host, port)  # 替换为实际的服务器 IP 或主机名
        filename = self.new_version_number  # 选择下载的可执行程序名称
        self.path = os.getcwd()  # 下载路径/home/huaming/Desktop/hxs/iCareProject_plus
        # 创建TCP套接字并连接到服务器
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect(server_address)
            except:
                logger.debug('连接被拒绝，请检查服务器地址和端口')
                return False
            # 发送请求下载文件
            try:
                DOWNLOAD_time = datetime.datetime.now()
                user_sip = config.get('sipnum', 'sipnum')
                nation = config.get('address', 'nation')
                province = config.get('address', 'province')
                city = config.get('address', 'city')
                adreess = nation + province + city
                # 自定义协议
                sock.sendall(f'DOWNLOAD？{filename}#{user_sip}#{DOWNLOAD_time}#{adreess}'.encode())
            except:
                logger.debug('向服务器发送请求时出错。')
                return
            self.file_path = os.path.join(self.path, filename)

            # 接收文件数据并写入本地文件
            with open(self.file_path, 'wb') as f:
                while True:
                    data = sock.recv(1024)
                    if not data:
                        break
                    f.write(data)
            if 'version' not in config.sections():
                config.add_section('version')
            config.set('version', 'number', f'{filename}')
            with open(ini_path, 'w') as f:
                config.write(f)
                logger.debug(f'最新版本{filename}写入文件保存成功')
                # self.Aboutupdates_view.label_3.setText(f'版本号：{filename}')
            # 授予执行权限，使其成为允许执行文件
            os.chmod(self.file_path, 0o755)
            # 关闭连接
            sock.close()
            logger.debug(f'最新版本{filename}已成功下载成功')
            return True
            # select = QMessageBox.information(self, '提示', f'最新版本{filename}下载成功，需重启后安装',
            #                                  QMessageBox.Yes | QMessageBox.No)
        #     if select == QMessageBox.Yes:
        #         # 进入下载更新界面，包含按钮立即更新和定时更新
        #         logger.debug('重新启动最新版本')
        #         # os.system(f'/home/huaming/Desktop/hxs/iCareProject_4.0/{filename}')
        #         # 备份
        #         try:
        #             # # 备份当前程序和数据
        #             # self.backup_files()
        #             # 启动最新版本程序
        #             os.spawnv(os.P_NOWAIT, filename, [filename])
        #             # 安全退出当前程序
        #             sys.exit(0)
        #         except Exception:
        #             # 启动新程序异常，回滚备份
        #             # self.restore_files()
        #             # os.spawnv(os.P_NOWAIT, self.current_version_number, [self.current_version_number])
        #             raise  # 将异常继续抛出，以便程序停止执行
        # return

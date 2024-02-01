#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""硬件设备数据相关功能接口"""
import time

from PyQt5.QtCore import QThread, pyqtSignal

from lib.broadcast_function import text_to_speech
from lib.machine_systems.get_sip_cpuid import get_sip, get_cpuid
from lib.requests_function.requests_server import save_machine_reports


class HardwareMonitoringThread(QThread):
    send_hardware_data = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.electricity = 30

    def get_electricity(self):
        """获取机器人电量"""
        # 模拟电量衰减
        # self.electricity -= 1
        return self.electricity

    def get_report(self):
        report = {
            "电池寿命": {
                "预计使用时间": "3小时",
            },
            "电机状态": {
                "左侧电机": "正常",
                "右侧电机": "正常",
            },
            "传感器状态": {
                "视觉传感器": "正常",

            },
            "系统运行状态": {
                "内存占用率": "32%",
            }
        }
        return str(report)

    def run(self):
        while True:
            electricity = self.get_electricity()

            if electricity == 20:
                # 电量低于20%的时候可以语言提示用户给机器人充电
                text_to_speech(text=f"电量低于20%,请及时给机器设备进行充电", filename='identify_result')
            elif electricity == 10:
                # 电量低于10%的时候向服务端发送机器人状态报告,进入低电量省电模式，触发自动导航充电功能
                save_machine_reports(sip=get_sip(), cpuid=get_cpuid(), report=self.get_report(),
                                     electricity=self.electricity)
            elif electricity == 5:
                # 电量低于5%的时候，进行强制关机处理
                print('电量低于5%，10秒后进行强制关机')
                break
            self.send_hardware_data.emit(self.electricity)
            # 获取机器人服务在线和离线时长
            # get_servertime()
            time.sleep(60)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
import threading

from PyQt5.QtCore import QThread, pyqtSignal


class HardwareGetData(QThread):
    send_result = pyqtSignal(str, str)  # 发送的信号现在包含两个参数，一个是消息，一个是传感器标识符

    def __init__(self):
        super().__init__()
        self.locks = {
            'DHT11': threading.Lock(),
            'MAX6675': threading.Lock(),
            'mlx90614': threading.Lock(),
            'MPU6050': threading.Lock(),
            'sr04': threading.Lock(),
            'usart': threading.Lock()
        }
        self.processes = {}  # 用于存储每个传感器对应的进程

    def output_reader(self, identifier, process):
        """线程函数，循环读取并发送流输出"""
        stdout_stream = process.stdout
        stderr_stream = process.stderr

        # 处理标准输出
        while True:
            line = stdout_stream.readline()
            if not line:
                break
            with self.locks[identifier]:
                message = line.decode().strip()
                self.send_result.emit(message, identifier)

        # 处理标准错误
        while True:
            line = stderr_stream.readline()
            if not line:
                break
            with self.locks[identifier]:
                error_message = line.decode().strip()
                self.send_result.emit(error_message, identifier)

        process.wait()  # 等待进程结束
        self.processes.pop(identifier, None)  # 清理已结束的进程记录

    def start_sensor(self, identifier, command):
        try:
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.processes[identifier] = process  # 存储进程以便管理

            # 创建并启动一个线程来监测并打印标准输出信息
            output_thread = threading.Thread(target=self.output_reader, args=(identifier, process))
            output_thread.daemon = True
            output_thread.start()

        except Exception as e:
            self.send_result.emit(f"启动时出错 {identifier}: {e}", identifier)

    def start_DHT11(self):
        self.start_sensor('DHT11', ['sudo', 'DHT11'])

    def start_MAX6675(self):
        self.start_sensor('MAX6675', ['sudo', 'MAX6675'])

    def start_mlx90614(self):
        self.start_sensor('mlx90614', ['sudo', 'mlx90614'])

    def start_MPU6050(self):
        self.start_sensor('MPU6050', ['sudo', 'MPU6050'])

    def start_sr04(self):
        self.start_sensor('sr04', ['sudo', 'sr04'])

    def start_usart(self):
        self.start_sensor('usart', ['sudo', 'usart'])

    def stop_sensor(self, identifier):
        if identifier in self.processes:
            process = self.processes[identifier]
            try:
                output = subprocess.check_output(['pgrep', '-P', str(process.pid)])
                child_pids = [int(pid) for pid in output.split()]
                child_pids.append(process.pid)
                subprocess.run(['kill'] + [str(pid) for pid in child_pids])
                self.processes.pop(identifier, None)
                print(f"停止 {identifier}")
            except subprocess.CalledProcessError:
                print(f"无法停止 {identifier}，进程可能已经结束")
        else:
            print(f"没有正在运行的进程 {identifier}")


class SensorSelfCheck:
    def __init__(self):
        self.thresholds = {
            'DHT11': {
                'temperature': (0, 50),  # 温度的预期范围
                'humidity': (20, 80)  # 湿度的预期范围
            },
            'MAX6675': {
                'temperature': (0, 1000)  # 温度的预期范围
            },
            'mlx90614': {
                'temperature': (0, 100)  # 温度的预期范围
            },
            'MPU6050': {
                'acceleration': (-9.8, 9.8),  # 加速度的预期范围
                'gyroscope': (-250, 250)  # 陀螺仪的预期范围
            },
            'sr04': {
                'distance': (0, 400)  # 距离的预期范围
            },
            'usart': {
                'data': (0, 1023)  # 数据的预期范围
            }
        }

    def check_sensor_data(self, identifier, data):
        if identifier in self.thresholds:
            for key, value in data.items():
                if key in self.thresholds[identifier]:
                    expected_range = self.thresholds[identifier][key]
                    if not self.is_within_range(value, expected_range):
                        self.generate_fault_report(identifier, key, value, expected_range)
        else:
            print(f"不支持的传感器类型 {identifier}")

    @staticmethod
    def is_within_range(value, expected_range):
        return expected_range[0] <= value <= expected_range[1]

    def generate_fault_report(self, identifier, key, value, expected_range):
        fault_report = f"传感器{identifier}的{key}数据异常！当前值：{value}，预期范围：{expected_range}"
        # 在此处添加将故障报告发送到后台的代码
        print(fault_report)  # 打印故障报告供调试使用

# self_check = SensorSelfCheck()
# self_check.check_sensor_data('DHT11', {'temperature': 25, 'humidity': 60})
# self_check.check_sensor_data('MPU6050', {'acceleration': 10, 'gyroscope': 200})
# self_check.check_sensor_data('sr04', {'distance': 450})

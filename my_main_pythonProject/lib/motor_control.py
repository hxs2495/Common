"""小车电机控制功能接口"""
import serial
from loguru import logger


class ConTrol:
    def __init__(self):
        logger.debug('初始化连接通信端口')
        self.arduino = serial.Serial('/dev/ttyACM0', 57600)

        self.record_functions = {
            '前': self.motor_forward,
            '过来': self.motor_forward,
            '后': self.motor_backward,
            '回去': self.motor_backward,
            '左': self.motor_left,
            '右': self.motor_right,
            '停': self.motor_stop,
        }

    # 停止电机
    def motor_stop(self):
        logger.debug('停止')
        self.arduino.write(b'0')

    # 控制电机正转
    def motor_forward(self):
        logger.debug('前进')
        self.arduino.write(b'1')

    # 控制电机反转
    def motor_backward(self):
        logger.debug('向后')
        self.arduino.write(b'2')

    # 控制电机左转
    def motor_left(self):
        logger.debug('向左')
        self.arduino.write(b'3')

    # 控制电机右转
    def motor_right(self):
        logger.debug('向右')
        self.arduino.write(b'4')

    def quit_control(self):
        logger.debug('退出控制')
        # self.arduino.write(b'0')
        self.arduino.close()

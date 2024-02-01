import wiringpi as wp
from loguru import logger


class MotorController:
    PWMA = 3
    AIN2 = 4
    AIN1 = 6
    BIN1 = 9
    BIN2 = 10
    PWMB = 13
    speed = 150

    def __init__(self):
        # 初始化wiringPi
        if wp.wiringPiSetup() == -1:
            logger.debug("初始化成功")
        else:
            logger.debug("初始化成功")

        # 设置引脚模式
        wp.pinMode(self.AIN1, 1)
        wp.pinMode(self.AIN2, 1)
        wp.pinMode(self.BIN1, 1)
        wp.pinMode(self.BIN2, 1)

        # 创建软件PWM
        wp.softPwmCreate(self.PWMA, 0, 255)
        wp.softPwmCreate(self.PWMB, 0, 255)
        logger.debug("软件PWM创建成功")

    def set_speed(self, speed):
        self.speed = speed

    def go_ahead(self):
        wp.softPwmWrite(self.PWMA, self.speed)
        wp.softPwmWrite(self.PWMB, self.speed)
        wp.digitalWrite(self.BIN1, 1)
        wp.digitalWrite(self.BIN2, 0)
        wp.digitalWrite(self.AIN1, 1)
        wp.digitalWrite(self.AIN2, 0)
        logger.debug("前进")

    def go_back(self):
        wp.softPwmWrite(self.PWMA, self.speed)
        wp.softPwmWrite(self.PWMB, self.speed)
        wp.digitalWrite(self.BIN1, 0)
        wp.digitalWrite(self.BIN2, 1)
        wp.digitalWrite(self.AIN1, 0)
        wp.digitalWrite(self.AIN2, 1)
        logger.debug("后退")

    def turn_left(self):
        wp.softPwmWrite(self.PWMB, self.speed)
        wp.digitalWrite(self.BIN1, 1)
        wp.digitalWrite(self.BIN2, 0)
        logger.debug("左转")

    def turn_right(self):
        wp.softPwmWrite(self.PWMA, self.speed)
        wp.digitalWrite(self.AIN1, 1)
        wp.digitalWrite(self.AIN2, 0)
        logger.debug("右转")

    def stop(self):
        wp.softPwmWrite(self.PWMA, 0)
        wp.digitalWrite(self.BIN1, 0)
        wp.digitalWrite(self.AIN1, 0)
        wp.digitalWrite(self.AIN2, 0)
        logger.debug("停止")


# if __name__ == '__main__':
#     try:
#         # 创建MotorController对象
#         motor_controller = MotorController()
#         # 控制机器人运动
#         motor_controller.go_ahead()
#         motor_controller.turn_left()
#         motor_controller.stop()

#         motor_controller.set_speed(150)
#         motor_controller.turn_left()  # 在150的速度下原地左转

#     except Exception as e:
#         # 错误处理
#         logger.debug("发生错误:", str(e))

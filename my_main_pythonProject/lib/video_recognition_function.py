# -*- coding: utf-8 -*-
"""视频识别监测功能接口"""
import datetime
import socket
import time

from PyQt5.QtCore import QThread, pyqtSignal
from loguru import logger

from lib.machine_systems.get_sip_cpuid import get_sip
from lib.machine_systems.hardware_monitoring_function import HardwareMonitoringThread
from lib.requests_function.requests_server import upload_file, get_server_count
from lib.wifi_function import WifiFunction


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


class VideoRecognitionThread(QThread):
    send_control_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.wifi = WifiFunction()

    def start_video_recognition(self):
        """启动视频监测功能函数"""
        logger.debug('正在启动摄像头进行监测')
        # fall = "yolov5fall/fall.pt"
        # opt = parse_opt(fall)
        # main(opt)
        time.sleep(10)
        logger.debug('监测到老人摔倒，开启警报倒计时模式')
        return True

    #     # cap = cv2.VideoCapture(0)
    #     #
    #     # while True:
    #     #     _, image = cap.read()
    #     #     if PI_fall().ImageDetect(image) == 1:
    #     #         logger.debug('监测到老人摔倒，开启警报模式')
    #     #         cap.release()
    #     #         break
    #
    #     def countdown(t):
    #         if t == 0:
    #             logger.debug('正在连通后台')
    #             top.destroy()
    #             connect_background()
    #         else:
    #             label.config(text='倒计时 {} 秒'.format(t))
    #             top.after(1000, countdown, t - 1)
    #
    #     def confirm():
    #         logger.debug('立即连通后台')
    #         top.destroy()
    #         connect_background()
    #
    #     def cancel():
    #         logger.debug('点击取消后台进入监测状态')
    #         top.destroy()
    # sys.exit()

    # # text_to_speech(text='监测到老人摔倒，开启警报模式，开始倒计时',filename='FallBroadcast')
    # top = tk.Tk()
    # top.title('倒计时')
    #
    # width = 200
    # height = 150
    # x = (top.winfo_screenwidth() - width) // 2
    # y = (top.winfo_screenheight() - height) // 2
    # top.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    #
    # label = tk.Label(top, text='倒计时 10 秒', font=('Arial', 20))
    # label.pack(pady=20)
    #
    # button_frame = tk.Frame(top)
    # button_frame.pack(pady=10)
    #
    # confirm_button = tk.Button(button_frame, text='确认', command=confirm)
    # confirm_button.pack(side='left', padx=10)
    #
    # cancel_button = tk.Button(button_frame, text='取消', command=cancel)
    # cancel_button.pack(side='right', padx=10)
    #
    # top.after(1000, countdown, 10)
    #
    # top.mainloop()

    def send_image_to_redis(self, imagepath):
        """发送紧急情况图片到后台进行存储，用于视频识别训练"""
        # send_image_to_redis(imagepath=imagepath)
        upload_file(file_path=imagepath)

    def get_server_count(self):
        """获取用户剩余服务额度"""
        count = get_server_count().get("customer_server_count")
        if count <= 0:
            logger.debug(f'后台服务额度为{count}，不支持进行后台客服服务，请进行会员充值服务额度')
            return False
        elif count >= 1:
            logger.debug(f'后台服务额度为{count}，支持进行后台客服服务')
            # self.connect_background_server()
            return count

    @count_server_time
    def connect_background_server(self, method='video'):
        """连接后台客服服务，实现客服接管机器人走形控制系统"""
        global sk
        count = self.get_server_count()
        if not count:
            return

        try:
            # 判断网络类型，根据不同类型采用不同连接方式
            res, _ = self.wifi.is_ipv6_or_ipv4()
            if res:
                logger.debug("网络类型：IPv6")
                # 创建IPv6套接字
                sk = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                # 连接服务器
                sk.connect(("240e:361:824:bb00:8c7b:e54b:df9c:bb06", 8888))
            else:
                logger.debug("网络类型：IPv4")
                # 创建IPv4套接字
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.connect(('192.168.1.137', 8888))

            # msg = sipnum.split(':')[1][0:4]
            hardwaremonitoringthread = HardwareMonitoringThread()
            electricity = hardwaremonitoringthread.get_electricity()
            sipnum = get_sip()
            data_dict = {'sipnum': sipnum, 'electricity': electricity, 'method': method}
            sk.sendall(str(data_dict).encode('utf-8'))
            # 确认数据全部发送
            sk.shutdown(socket.SHUT_WR)
            logger.debug(f'向服务端发送数据：{data_dict}')

            # # 电话呼叫线程
            # self.linphonecthread = LinphonecThread()
            # self.linphonecthread.start()
            # self.linphonecthread.video_call(sipnum=1002)

            while True:
                data = sk.recv(1024).decode('utf-8')
                # 使用replace()方法替换'\n'为空字符串''
                data = data.replace('\n', '')
                if not data:
                    continue
                logger.debug(f'接收服务端数据：{data}')
                if '0' in data:
                    logger.debug('后台客服接管已断开，本次服务到此结束')
                    self.send_control_result.emit('结束')
                    # update_count = {'method': 'get_data',
                    #                 'sql': f"update host_information set customer_server_count=customer_server_count-1 where cpuid='{count}';"}
                    # get_or_send_mysqldata(data=update_count)
                    # logger.debug('额度计数更新成功')
                    break
                elif 'w' in data:
                    logger.debug('前进')
                    self.send_control_result.emit('前进')
                elif 's' in data:
                    logger.debug('后退')
                    self.send_control_result.emit('后退')
                elif 'a' in data:
                    logger.debug('向左')
                    self.send_control_result.emit('向左')
                elif 'd' in data:
                    logger.debug('向右')
                    self.send_control_result.emit('向右')
                elif 'z' in data:
                    logger.debug('停止')
                    self.send_control_result.emit('停止')

        except socket.error as e:
            logger.debug('连接服务器失败:', e)
        finally:
            logger.debug('正在释放计算机资源')
            # 释放资源
            sk.close()

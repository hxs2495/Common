# -*- coding: utf-8 -*-
"""opencv视频人像采集功能接口"""
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

# from db.db_handler import send_image_to_redis


class VideoPlayer:
    def __init__(self, label):
        self.portrait_label = label
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_frame)

    def start_video(self):
        # 打开摄像头
        self.cap = cv2.VideoCapture(0)
        # 启动定时器
        self.timer.start(30)

    def stop_video(self):
        # 停止定时器
        self.timer.stop()
        # 读取最后一帧视频帧
        ret, frame = self.cap.read()
        if ret:
            # 转换为QImage并显示
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.portrait_label.setPixmap(pixmap)
            # 保存最后一帧图片到本地
            cv2.imwrite("conf/icon/user.png", frame)

        # 释放摄像头资源
        self.cap.release()

    def display_frame(self):
        # 读取视频帧
        ret, frame = self.cap.read()
        if ret:
            # 将视频帧转换成QImage格式
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            # 显示视频帧
            self.portrait_label.setPixmap(pixmap)

# def capture_photo(num, save_path, delay_time=1):
#     cap = cv2.VideoCapture(0)
#     flag = cap.isOpened()
#     index = 1
#     while (flag and index <= num):
#         ret, frame = cap.read()
#         cv2.imwrite(save_path + str(index) + ".jpg", frame)
#         print("save" + str(index) + ".jpg successfuly!")
#         send_image_to_redis(imagepath=save_path + str(index) + ".jpg")
#         index += 1
#     cap.release()

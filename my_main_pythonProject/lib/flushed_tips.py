#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time

from PyQt5.QtCore import QThread, pyqtSignal
from loguru import logger

from db.db_handler import execute_sql


class FlushedTips(QThread):
    tips_label_received = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            random_delay = random.randint(30, 60)  # 生成30到60之间的随机数作为延迟时间
            time.sleep(random_delay)  # 随机延迟时间
            reminders = execute_sql(sql=f'SELECT tips_text FROM tipslist ORDER BY RANDOM() LIMIT 1;')
            reminder = '温馨提示：' + reminders[0].get('tips_text', '')
            # self.tips_label.setText(reminder)
            self.tips_label_received.emit(reminder)
            logger.debug("更新温馨提示")

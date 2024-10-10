# -*- coding: utf-8 -*-
import sys
import time

import pandas as pd
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow

from untitled import Ui_MainWindow

HEADERS = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


class MyWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_conf()
        self.pushButton.clicked.connect(self.start_search)
        self.current_page = 0

    def load_conf(self):
        self.centralwidget.setStyleSheet("#centralwidget{border-image:url(background.jpg);}")

    def start_search(self):
        page_count = self.spinBox.value()
        song_id = self.lineEdit_2.text().strip()
        if not song_id:
            self.plainTextEdit.appendPlainText('请输入歌曲对应ID')
            return

        comments_data = []
        for i in range(page_count):
            state = self.get_song_comments(page=i * 20, song_id=song_id, comments_data=comments_data)
            if not state:
                break  # 失败时退出循环
            self.current_page = i + 1
            self.progressBar.setValue(int(self.current_page / page_count * 100))
            time.sleep(1)
        self.plainTextEdit.appendPlainText('\n---------------爬取完成---------------')
        self.save_to_excel(comments_data)

    def get_song_comments(self, page=0, song_id='', comments_data=None):
        url = f'https://music.163.com/api/v1/resource/comments/R_SO_4_{song_id}?limit=20&offset={page}'
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            result = response.json()
        except requests.RequestException:
            self.plainTextEdit.appendPlainText("网络请求失败: 请检查网络连接状况")
            return False

        items = result.get('comments', [])
        if not items:
            self.plainTextEdit.appendPlainText('没有评论信息。')
            return True  # 没有评论，但仍然成功

        for item in items:
            user_info = self.extract_comment_info(item)
            comments_data.append(user_info)
            self.plainTextEdit.appendPlainText(
                f'用户名:{user_info["username"]} 评论时间:{user_info["date"]} '
                f'评论内容:{user_info["comment"]} 评论点赞数:{user_info["praise"]}'
            )
        return True

    def save_to_excel(self, comments_data):
        headers = ['用户名', '用户ID', '评论内容', '评论时间', '评论点赞数',
                   '用户年龄', '用户性别', '用户所在地', '个人介绍']
        df = pd.DataFrame(comments_data)
        df.to_excel('comment.xlsx', index=False, header=headers)
        self.plainTextEdit.appendPlainText('数据已保存')

    def extract_comment_info(self, item):
        user_name = item['user']['nickname'].replace(',', '，')
        user_id = str(item['user']['userId'])
        comment = item['content'].strip().replace('\n', '').replace(',', '，')
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['time'] // 1000))
        praise = str(item['likedCount'])
        user_message = self.get_user_info(user_id)

        return {
            "username": user_name,
            "user_id": user_id,
            "comment": comment,
            "date": date,
            "praise": praise,
            "age": user_message.get('age', '无'),
            "gender": user_message.get('gender', '无'),
            "city": user_message.get('city', '无'),
            "introduce": user_message.get('sign', '无').strip().replace('\n', '').replace(',', '，')
        }

    def get_user_info(self, user_id):
        url = f'https://music.163.com/api/v1/user/detail/{user_id}'
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            user_data = response.json().get('profile', {})
            return {
                'gender': self._get_gender(user_data),
                'age': self._calculate_age(user_data),
                'city': user_data.get('city', '无'),
                'sign': user_data.get('signature', '无').strip().replace('\n', '').replace(',', '，')
            }
        except requests.RequestException:
            return {'gender': '无', 'age': '无', 'city': '无', 'sign': '无'}

    def _get_gender(self, profile):
        gender_map = {0: '未知', 1: '男', 2: '女'}
        print(profile)
        return gender_map.get(profile.get('gender'), '无')

    def _calculate_age(self, profile):
        birthday = profile.get('birthday', -1)
        if birthday > 0:
            current_year = time.localtime().tm_year
            age = current_year - time.localtime(birthday // 1000).tm_year
            return max(age, 0)
        return '无'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MyWindow()
    viewer.show()
    sys.exit(app.exec_())

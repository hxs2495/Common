"""
主控公共功能方法接口
"""
import configparser
import datetime
import os

from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy
from loguru import logger

BASE_PROJECT_DIR = os.getcwd()  # /home/hxs/PycharmProjects/maincontrol_plus
config = configparser.ConfigParser()  # 类实例化
# 定义文件路径
ini_path = os.path.join(BASE_PROJECT_DIR, 'conf/conf.ini')

config.read(ini_path, encoding='UTF-8')


def save_config():
    """保存配置文件conf.ini"""
    with open(ini_path, 'w') as f:
        config.write(f)  # 将配置写入文件


def day_logger():
    """生成写入日志"""
    logger.add('./AppData/log/{time:YYYY-MM-DD}/{time:YYYY-MM-DD}.log', rotation="1 day", retention='365 days',
               level='DEBUG', compression="zip")


# def read_language(Languages):
#     """读取 JSON 文件"""
#     with open('db/language.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     # 获取 data 中所有的键
#     keys = data.keys()
#     language = data.get(Languages)
#     return keys, language


def load_file_content(filepath, controlname):
    """优化读取文件通用方法"""
    # 逐行读取文件内容并显示在控件中
    with open(filepath, 'r', encoding="utf8") as file:
        for line in file:
            line = line.strip()
            if line:  # 如果当前行非空行，则添加到 QTextEdit 控件中
                controlname.append(line)


def write_file_data(filepath, data):
    """优化写入接收文件通用方法"""
    with open(filepath, 'w', encoding='UTF-8') as file:
        file.writelines(f'{data}\n' for data in data)


def get_age_and_gender_by_id_card(id_card):
    """将身份证号转为性别和年龄"""
    # 根据身份证号获取年龄和性别
    age = 0
    gender = ''
    try:
        birth_year = int(id_card[6:10])
        birth_month = int(id_card[10:12])
        birth_day = int(id_card[12:14])
        today = datetime.date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        if int(id_card[-2]) % 2 == 0:
            gender = '女'
        else:
            gender = '男'
    except:
        pass
    return str(age), gender


# # 后期根据与硬件对接获取
# def get_electricity():
#     """获取机器人电量"""
#     electricity = '100'
#     return electricity


def load_urlview(widget, url):
    """加载显示url通用方法"""
    layout = QVBoxLayout(widget)
    browser = QWebEngineView()
    browser.setUrl(QUrl(url))
    browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置大小策略
    layout.addWidget(browser)


def load_htmlview(frame, file_path):
    """加载显示html页面通用方法"""
    path = os.path.join(BASE_PROJECT_DIR, file_path)
    layout = frame.layout()  # 获取已存在的布局
    if layout is None:
        layout = QVBoxLayout(frame)  # 创建新的布局
        browser = QWebEngineView(frame)
        # 设置 WebEngine 视图的透明背景
        browser.setAttribute(Qt.WA_TranslucentBackground)
        # file_path = r'/home/hxs/PycharmProjects/maincontrol_plus/static/weather.html'
        browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        browser.load(QtCore.QUrl.fromLocalFile(path))
        layout.addWidget(browser)

# 查询操作
# result = execute_sql("SELECT * FROM blacklist")
# print(result)
# 插入操作
# execute_sql("INSERT INTO blacklist (name) VALUES (?)", "张三")
# 更新操作
# execute_sql("UPDATE blacklist SET name = ? WHERE id = ?", "李四", 1)
# 删除操作
# execute_sql("DELETE FROM blacklist WHERE id = ?", 1)


# def check_time():
#     """获取在线北京时间作为校准"""
#     url = 'https://www.baidu.com'
#     res = requests.get(url)
#     standard_time = res.headers['date']
#     standard_time = datetime.datetime.strptime(standard_time, '%a, %d %b %Y %H:%M:%S GMT')
#     standard_time = standard_time + datetime.timedelta(hours=8)
#     # 输出北京时间
#     logger.debug(f"当前北京时间为：{standard_time}")
#     # 计算本地时间和标准时间的偏差
#     local_time = datetime.datetime.now()
#     local_time1 = local_time.strftime("%Y-%m-%d %H:%M:%S")
#     logger.debug(f"当前本地时间为：{local_time1}")
#     delta = standard_time - local_time
#     if abs(delta.total_seconds()) > 30:
#         logger.debug("时间出现偏差，正在校正！")
#         time_str = standard_time.strftime('%Y-%m-%d %H:%M:%S')
#         start_correction_time(time_str=time_str)
#     else:
#         logger.debug("本地时间与北京时间同步，无需校正")
#
#
# def start_correction_time(time_str):
#     time_command = 'date -s "' + time_str + '"'
#     # 以管理员权限运行终端命令
#     os.system('sudo -s')
#     # 输入密码
#     password = '1'
#     command = f'echo {password} | sudo -S {time_command}'
#     os.system(command)
#     # 退出管理员权限
#     os.system('exit')

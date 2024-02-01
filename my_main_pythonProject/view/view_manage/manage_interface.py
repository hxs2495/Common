from PyQt5.QtCore import QRunnable, QThreadPool
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow

from conf import setting
from lib.db_function.db_interface import DatabaseManager
from view.view_manage.manage_untitled import Ui_MainWindow as ManageMixinS
from ..chat_view import chat_interface
from ..init_view import init_interface
from ..main_view import main_interface
from ..music_view import music_interface
from ..setting_view import setting_interface


class InitDatabaseTask(QRunnable):
    def __init__(self, db_url):
        super().__init__()
        self.db_url = db_url

    def run(self):
        db_manager = DatabaseManager(self.db_url)
        db_manager.create_database()


class Manage_InterFace(ManageMixinS, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.is_init = False

        self.pages = {}
        self.init_pages()

        # self.Pivot.addItem("init_view", text="初始化", onClick=lambda: self.load_page('init_view'))
        # self.Pivot.addItem("main_view", text="主界面", onClick=lambda: self.load_page('main_view'))
        # self.Pivot.addItem("chat_view", text="聊天界面", onClick=lambda: self.load_page('chat_view'))

        self.show_window()

        # 初始化创建数据库和表结构
        # 初始化创建数据库和表结构
        thread_pool = QThreadPool.globalInstance()
        init_task = InitDatabaseTask(setting.db_url)
        thread_pool.start(init_task)

    def init_pages(self):
        self.pages['init_view'] = init_interface.Init_InterFace()
        self.pages['init_view'].switch_main_interface.connect(lambda: self.load_page('main_view'))

        self.pages['main_view'] = main_interface.Main_Interface()
        self.pages['main_view'].switch_interface.connect(self.main_switch_interface)

        self.pages['chat_view'] = chat_interface.Chat_InterFace()
        self.pages['chat_view'].switch_main_interface.connect(lambda: self.load_page('main_view'))

        self.pages['setting_view'] = setting_interface.Setting_InterFace()

        self.pages['music_view'] = music_interface.Music_InterFace()
        self.pages['music_view'].switch_main_interface.connect(lambda: self.load_page('main_view'))


        for page in self.pages.values():
            self.PopUpAniStackedWidget.addWidget(page)

    def show_window(self):
        if self.is_init:
            self.load_page('init_view')
            return
        self.load_page('main_view')

    def load_page(self, page_name):
        self.PopUpAniStackedWidget.setCurrentWidget(self.pages[page_name])

    # 窗口大小发生变化时自动触发该函数，重置背景
    def resizeEvent(self, event):
        # 设置窗体背景图片
        palette = QPalette()
        brush = QBrush(QPixmap(setting.background_img).scaled(self.width(), self.height()))
        # brush = QBrush(QPixmap(config.get('imagepath', 'path')).scaled(self.width(), self.height()))
        palette.setBrush(QPalette.Background, brush)
        self.setPalette(palette)
        # 设置不影响其他控件背景
        self.setAutoFillBackground(True)

    def main_switch_interface(self, view_type):
        if view_type == "chat":
            self.load_page('chat_view')
        elif view_type == "music":
            self.load_page('music_view')

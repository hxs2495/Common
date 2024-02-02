from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow
from qfluentwidgets import FluentIcon, NavigationItemPosition

from view.chat_view import chat_interface
from view.music_view import music_interface
from view.new_main_view.new_main_untitled import Ui_MainWindow as new_mainMixinS
from view.radio_view import radio_interface
from view.setting_view import setting_interface


class NewMainInterFace(new_mainMixinS, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pages = {}
        self.init_pages()
        self.init_setup()
        self.load_icon()

    def init_pages(self):
        # self.pages['init_view'] = init_interface.Init_InterFace()
        # self.pages['init_view'].switch_main_interface.connect(lambda: self.load_page('main_view'))
        #
        # self.pages['main_view'] = main_interface.Main_Interface()
        # # self.pages['main_view'].switch_interface.connect(self.main_switch_interface)
        #
        self.pages['chat_view'] = chat_interface.ChatInterFace()
        # self.pages['chat_view'].switch_main_interface.connect(lambda: self.load_page('main_view'))

        self.pages['setting_view'] = setting_interface.SettingInterFace()

        self.pages['music_view'] = music_interface.MusicInterFace()

        # self.pages['music_view'].switch_main_interface.connect(lambda: self.load_page('main_view'))

        self.pages['radio_view'] = radio_interface.RadioInterFace()

        for page in self.pages.values():
            self.PopUpAniStackedWidget_3.addWidget(page)

    def load_page(self, page_name):
        self.PopUpAniStackedWidget.setCurrentIndex(1)
        self.PopUpAniStackedWidget_3.setCurrentWidget(self.pages[page_name])

    def init_setup(self):
        self.PopUpAniStackedWidget.setCurrentIndex(0)
        self.PopUpAniStackedWidget_2.setCurrentIndex(0)
        self.PopUpAniStackedWidget_3.setCurrentIndex(0)

        self.NavigationInterface.addItem(
            routeKey="chat",
            icon=FluentIcon.CHAT,
            text="聊天",
            tooltip="聊天",
            position=NavigationItemPosition.TOP,
            onClick=lambda: self.load_page(page_name="chat_view")

        )
        self.NavigationInterface.addItem(
            routeKey="music",
            icon=FluentIcon.MUSIC,
            text="音乐",
            tooltip="音乐",
            position=NavigationItemPosition.SCROLL,
            onClick=lambda: self.load_page(page_name="music_view")

        )
        self.NavigationInterface.addItem(
            routeKey="radio",
            icon=FluentIcon.ALBUM,
            text="电台",
            tooltip="电台",
            position=NavigationItemPosition.SCROLL,
            onClick=lambda: self.load_page(page_name="radio_view")

        )
        self.NavigationInterface.addItem(
            routeKey="video",
            icon=FluentIcon.VIDEO,
            text="视频",
            tooltip="视频",
            position=NavigationItemPosition.SCROLL,
            onClick=lambda: print("视频")

        )
        self.NavigationInterface.addItem(
            routeKey="setting",
            icon=FluentIcon.SETTING,
            text="设置",
            tooltip="设置",
            position=NavigationItemPosition.BOTTOM,
            onClick=lambda: self.load_page(page_name="setting_view")
        )

        self.NavigationInterface.addItem(
            routeKey="return",
            icon=FluentIcon.RETURN,
            text="返回",
            tooltip="返回",
            position=NavigationItemPosition.BOTTOM,
            onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(0)
        )

        # 捕获鼠标点击事件
        # self.frame_2.mousePressEvent = self.frameClicked
        self.home_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget_2.setCurrentIndex(0))
        self.pushButton_2.clicked.connect(lambda: self.PopUpAniStackedWidget_2.setCurrentIndex(1))

        self.music_player_pushButton.clicked.connect(lambda: self.load_page(page_name="music_view"))
        self.chat_player_pushButton.clicked.connect(lambda: self.load_page(page_name="chat_view"))
        self.radio_player_pushButton.clicked.connect(lambda: self.load_page(page_name="radio_view"))
        self.setting_player_pushButton.clicked.connect(lambda: self.load_page(page_name="setting_view"))

    def load_icon(self):

        # 设置按钮图标
        buttons = [(self.telephonecall_pushButton, 'test.png'),
                   (self.music_player_pushButton, 'test2.png'),
                   (self.chat_player_pushButton, 'test2.png'),
                   (self.radio_player_pushButton, 'test2.png'),
                   (self.music_player_pushButton_21, 'test.png'),
                   (self.music_player_pushButton_5, 'test.png'),
                   (self.music_player_pushButton_6, 'test.png'),
                   (self.setting_player_pushButton, 'test.png'),
                   (self.music_player_pushButton_19, 'test.png'),
                   (self.music_player_pushButton_16, 'test.png'),
                   (self.music_player_pushButton_14, 'test.png'),
                   (self.music_player_pushButton_17, 'test.png'),
                   (self.music_player_pushButton_20, 'test.png'),
                   (self.music_player_pushButton_15, 'test.png'),

                   ]
        common_button_style = """
            QPushButton {
                border: none;
                background-color: transparent;
            }
        """

        for button, icon in buttons:
            button.setStyleSheet(common_button_style)
            button.setIcon(QIcon(f'C:/PycharmProjects/my_main_pythonProject/conf/static/icon/{icon}'))
            button.setIconSize(button.size())

        self.PillPushButton.setIcon(FluentIcon.WIFI)
        self.PillPushButton_2.setIcon(FluentIcon.BLUETOOTH)
        self.PillPushButton_3.setIcon(FluentIcon.CONSTRACT)
        self.PillPushButton_4.setIcon(FluentIcon.BRIGHTNESS)
        self.PillPushButton_5.setIcon(FluentIcon.VOLUME)

    # 窗口大小发生变化时自动触发该函数，重置背景
    def resizeEvent(self, event):
        # 设置窗体背景图片
        palette = QPalette()
        brush = QBrush(
            QPixmap(r"C:\PycharmProjects\my_main_pythonProject\conf\static\material\14.jpg").scaled(self.width(),
                                                                                                    self.height()))
        # brush = QBrush(QPixmap(config.get('imagepath', 'path')).scaled(self.width(), self.height()))
        palette.setBrush(QPalette.Background, brush)
        self.setPalette(palette)
        # 设置不影响其他控件背景
        self.setAutoFillBackground(True)

    def frameClicked(self, event):
        if event.button() == Qt.LeftButton:
            print("Frame clicked!")
            # print("控件名称:", self.sender().objectName())  # 打印输出控件名称
        else:
            event.ignore()

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow

from view.test_view.test_untitled import Ui_MainWindow as TestMixinS


class Tset_InterFace(TestMixinS, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # self.TabBar.setTabsClosable(False)
        self.TabBar.tabAddRequested.connect(self.onTabAddRequested)

        self.TabBar.tabBarClicked.connect(self.onTabClicked)
        self.TabBar.tabCloseRequested.connect(self.TabBar.removeTab)

        # 捕获鼠标点击事件
        self.frame_2.mousePressEvent = self.frameClicked

    def onTabAddRequested(self):
        TabBar_count = self.TabBar.count()
        self.TabBar.addTab(routeKey=TabBar_count, text=f"hello{TabBar_count}",
                           icon=QIcon("C:\PycharmProjects\my_main_pythonProject\conf\static\icon\chat.png"))

    def onTabClicked(self, index: int):
        objectName = self.TabBar.currentTab().routeKey()
        print(objectName)
        # self.TabBar.removeTab(index=index)

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

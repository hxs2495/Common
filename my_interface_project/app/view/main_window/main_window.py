from PyQt5.QtWidgets import QMainWindow

from .main_untitled import Ui_MainWindow as MainMixinS
from ..init_view import init_interface
from ..second_view import second_interface


class MainWindow(MainMixinS, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pages = {}
        self.init_pages()

        self.PrimaryPushButton.clicked.connect(lambda: self.load_page('page1'))
        self.PrimaryPushButton_2.clicked.connect(lambda: self.load_page('page2'))

    def init_pages(self):
        self.pages['page1'] = init_interface.Init_InterFace()
        self.pages['page2'] = second_interface.Secord_Interface()

        for page in self.pages.values():
            self.PopUpAniStackedWidget.addWidget(page)

    def load_page(self, page_name):
        self.PopUpAniStackedWidget.setCurrentWidget(self.pages[page_name])

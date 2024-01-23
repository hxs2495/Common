from PyQt5.QtWidgets import QMainWindow
from qfluentwidgets import FluentIcon, NavigationItemPosition

from .main_untitled import Ui_MainWindow as MainMixinS
from ..init_view import init_interface
from ..second_view import second_interface
from ..setting_view import setting_interface


class MainWindow(MainMixinS, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pages = {}
        self.init_pages()
        self.NavigationInterface.setMenuButtonVisible(True)
        self.NavigationInterface.setReturnButtonVisible(True)
        self.NavigationInterface.addItem(
            routeKey="1",
            icon=FluentIcon.SETTING,
            text="界面1",
            onClick=lambda: self.load_page('page1'),
            position=NavigationItemPosition.TOP,
            tooltip="texttooltip"
        )
        self.NavigationInterface.addItem(
            routeKey="2",
            icon=FluentIcon.HELP,
            text="界面2",
            onClick=lambda: self.load_page('page2'),
            position=NavigationItemPosition.SCROLL,
            tooltip="texttooltip"
        )
        self.NavigationInterface.addItem(
            routeKey="4",
            icon=FluentIcon.AIRPLANE,
            text="界面2",
            onClick=lambda: self.load_page('page2'),
            position=NavigationItemPosition.SCROLL,
            tooltip="texttooltip"
        )
        self.NavigationInterface.addItem(
            routeKey="3",
            icon=FluentIcon.ADD,
            text="界面3",
            onClick=lambda: self.load_page('page3'),
            position=NavigationItemPosition.BOTTOM,
            tooltip="texttooltip"
        )
        self.PrimaryPushButton.clicked.connect(lambda: self.load_page('page1'))
        self.PrimaryPushButton_2.clicked.connect(lambda: self.load_page('page2'))
        self.PrimaryPushButton_3.clicked.connect(lambda: self.load_page('page3'))

        self.Pivot.addItem("Pivotmusic", text="界面1", onClick=lambda: self.load_page('page1'))
        self.Pivot.addItem("Pivotwifi", text="界面2", onClick=lambda: self.load_page('page2'))
        self.Pivot.addItem("Pivotwifi1", text="界面3", onClick=lambda: self.load_page('page3'))

        self.SegmentedWidget.addItem("Segmentedwifi1", text="界面1", onClick=lambda: self.load_page('page1'))
        self.SegmentedWidget.addItem("Segmentedwifi2", text="界面2", onClick=lambda: self.load_page('page2'))
        self.SegmentedWidget.addItem("Segmentedwifi3", text="界面3", onClick=lambda: self.load_page('page3'))

        self.SegmentedToggleToolWidget.addItem("SegmentedToggleTool1", icon=FluentIcon.MENU,
                                               onClick=lambda: self.load_page('page1'))
        self.SegmentedToggleToolWidget.addItem("SegmentedToggleTool2", icon=FluentIcon.HEADPHONE,
                                               onClick=lambda: self.load_page('page2'))
        self.SegmentedToggleToolWidget.addItem("SegmentedToggleTool3", icon=FluentIcon.FEEDBACK,
                                               onClick=lambda: self.load_page('page3'))

    def init_pages(self):
        self.pages['page1'] = init_interface.Init_InterFace()
        self.pages['page2'] = second_interface.Secord_Interface()
        self.pages['page3'] = setting_interface.Setting_InterFace()

        for page in self.pages.values():
            self.PopUpAniStackedWidget.addWidget(page)

    def load_page(self, page_name):
        self.PopUpAniStackedWidget.setCurrentWidget(self.pages[page_name])

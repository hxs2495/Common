# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hxs/VS_Projects/Common/my_interface_project/app/view/main_window/main_untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.PopUpAniStackedWidget = PopUpAniStackedWidget(self.centralwidget)
        self.PopUpAniStackedWidget.setObjectName("PopUpAniStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.PopUpAniStackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.PopUpAniStackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.PopUpAniStackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.PopUpAniStackedWidget, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PrimaryPushButton = PrimaryPushButton(self.centralwidget)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")
        self.horizontalLayout_2.addWidget(self.PrimaryPushButton)
        self.PrimaryPushButton_2 = PrimaryPushButton(self.centralwidget)
        self.PrimaryPushButton_2.setObjectName("PrimaryPushButton_2")
        self.horizontalLayout_2.addWidget(self.PrimaryPushButton_2)
        self.PrimaryPushButton_3 = PrimaryPushButton(self.centralwidget)
        self.PrimaryPushButton_3.setObjectName("PrimaryPushButton_3")
        self.horizontalLayout_2.addWidget(self.PrimaryPushButton_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.SegmentedWidget = SegmentedWidget(self.centralwidget)
        self.SegmentedWidget.setObjectName("SegmentedWidget")
        self.horizontalLayout.addWidget(self.SegmentedWidget)
        self.Pivot = Pivot(self.centralwidget)
        self.Pivot.setObjectName("Pivot")
        self.horizontalLayout.addWidget(self.Pivot)
        self.SegmentedToggleToolWidget = SegmentedToggleToolWidget(self.centralwidget)
        self.SegmentedToggleToolWidget.setObjectName("SegmentedToggleToolWidget")
        self.horizontalLayout.addWidget(self.SegmentedToggleToolWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.PopUpAniStackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PrimaryPushButton.setText(_translate("MainWindow", "界面1"))
        self.PrimaryPushButton_2.setText(_translate("MainWindow", "界面2"))
        self.PrimaryPushButton_3.setText(_translate("MainWindow", "界面3"))
from qfluentwidgets import Pivot, PopUpAniStackedWidget, PrimaryPushButton, SegmentedToggleToolWidget, SegmentedWidget

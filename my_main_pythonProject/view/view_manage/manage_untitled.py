# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Pivot = Pivot(self.centralwidget)
        self.Pivot.setObjectName("Pivot")
        self.gridLayout_2.addWidget(self.Pivot, 0, 0, 1, 1)
        self.SmoothScrollArea = SmoothScrollArea(self.centralwidget)
        self.SmoothScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SmoothScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.SmoothScrollArea.setObjectName("SmoothScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 377))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PopUpAniStackedWidget = PopUpAniStackedWidget(self.scrollAreaWidgetContents)
        self.PopUpAniStackedWidget.setObjectName("PopUpAniStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.PopUpAniStackedWidget.addWidget(self.page)
        self.gridLayout.addWidget(self.PopUpAniStackedWidget, 0, 0, 1, 1)
        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.SmoothScrollArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.PopUpAniStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
from qfluentwidgets import Pivot, PopUpAniStackedWidget, SmoothScrollArea
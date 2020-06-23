# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'chat_screen.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import ui_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(720, 785)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setGeometry(QRect(-1, 0, 851, 41))
        self.horizontalWidget.setStyleSheet(
            u"background-color: rgb(53, 52, 98);")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(80, 90, 201, 531))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(0, 40, 81, 401))
        self.verticalWidget.setStyleSheet(
            u"background-color: rgb(35, 36, 53);")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(self.verticalWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(22)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setSizeIncrement(QSize(30, 49))
        self.pushButton_4.setStyleSheet(u"image: url(:/test/images/bell.svg);\n"
                                        "color : rgb(255, 255, 255);\n"
                                        "font: 13pt \".AppleSystemUIFont\";")
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                        "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.verticalWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                        "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.verticalWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                        "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.verticalWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                        "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_8 = QPushButton(self.verticalWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                        "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.verticalWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                        "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.verticalWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                         "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(269, 90, 581, 531))
        self.scrollArea.setStyleSheet(u"background-color: rgb(240, 239, 238);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 579, 529))
        self.scrollAreaWidgetContents.setStyleSheet(
            u"background-color: rgb(240, 239, 238);")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 90, 51, 32))
        icon = QIcon()
        icon.addFile(u"images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        # ここから触ってみる
        self.pushButton.setCheckable(True)
        # シグナル・スロットの設定
        self.pushButton.toggled.connect(self.slot_button_toggled)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 95, 113, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalWidget.raise_()
        self.horizontalWidget.raise_()
        self.listWidget.raise_()
        self.scrollArea.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.pushButton.showMenu)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def slot_button_toggled(self, checked):
        """ ボタンがトグルされたときのスロット """
        if checked:
            self.lineEdit.setVisible(True)
        else:
            self.lineEdit.setVisible(False)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate(
            "MainWindow", u"\u3060\u3093\u30543\u5144\u5f1f", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u6700\u65b0\u60c5\u5831", None))
        self.pushButton_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u30c1\u30e3\u30c3\u30c8", None))
        self.pushButton_7.setText(QCoreApplication.translate(
            "MainWindow", u"\u8ab2\u984c", None))
        self.pushButton_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u30c1\u30fc\u30e0", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e88\u5b9a\u8868", None))
        self.pushButton_8.setText(QCoreApplication.translate(
            "MainWindow", u"\u901a\u8a71", None))
        self.pushButton_9.setText(QCoreApplication.translate(
            "MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
        self.pushButton_10.setText(QCoreApplication.translate(
            "MainWindow", u"\uff65\uff65\uff65", None))
        self.pushButton.setText("")
        # self.lineEdit.setText(QCoreApplication.translate(
        #     "MainWindow", u"\u691c\u7d22\u6b04", None))
        self.lineEdit.setText(QCoreApplication.translate(
            "MainWindow", "Hello", None))
    # retranslateUi

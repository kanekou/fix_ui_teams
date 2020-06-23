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
        MainWindow.resize(960, 1035)
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
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background-color: rgb(240, 239, 238);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 579, 529))
        self.scrollAreaWidgetContents.setStyleSheet(
            u"background-color: rgb(240, 239, 238);")
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 330, 131, 31))
        self.textEdit.setVisible(False)

        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(170, 330, 131, 31))
        self.textEdit_2.setVisible(False)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(310, 330, 113, 32))
        self.pushButton_11.setVisible(False)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 90, 51, 32))
        icon = QIcon()
        icon.addFile(u"images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        # オリジナル
        self.pushButton.setCheckable(True)
        # シグナル・スロットの設定
        self.pushButton.toggled.connect(self.slot_button_toggled)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 95, 113, 21))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 130, 113, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalWidget.raise_()
        self.horizontalWidget.raise_()
        self.listWidget.raise_()
        self.scrollArea.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.pushButton.showMenu)
        # self.pushButton_2.clicked.connect(self.pushButton_2.click)
        self.pushButton_2.clicked.connect(self.slot_button_clicked_to_view)
        self.pushButton_11.clicked.connect(self.slot_button_clicked_to_remove)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def slot_button_toggled(self, checked):
        if checked:
            self.lineEdit.setVisible(True)
        else:
            self.lineEdit.setVisible(False)

    def slot_button_clicked_to_view(self, clicked):
        if clicked:
            self.textEdit.setVisible(True)
            self.textEdit_2.setVisible(True)
            self.pushButton_11.setVisible(True)
            print("clicked to visible!")

    def slot_button_clicked_to_remove(self, clicked):
        self.textEdit.setVisible(False)
        self.textEdit_2.setVisible(False)
        self.pushButton_11.setVisible(False)
        print("clicked to not visible!")

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
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">invate user</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">group name</p></body></html>", None))
        self.pushButton_11.setText(
            QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton.setText("")
        self.lineEdit.setText(QCoreApplication.translate(
            "MainWindow", u"\u691c\u7d22\u6b04", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"NewChat", None))
        self.pushButton_2.setCheckable(True)
        # シグナル・スロットの設定

    # retranslateUi

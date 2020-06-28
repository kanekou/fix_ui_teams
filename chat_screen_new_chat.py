# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'chat_screen_new_chat.ui'
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


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(852, 557)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(80, 200, 191, 421))
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(0, 50, 81, 381))
        self.verticalWidget.setStyleSheet(
            u"background-color: rgb(35, 36, 53);")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButton = QToolButton(self.verticalWidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton.setStyleSheet(u"image: url(:/test/images/\u6700\u65b0\u60c5\u5831.png);\n"
                                      "")
        self.toolButton.setIconSize(QSize(88, 32))

        self.verticalLayout.addWidget(self.toolButton)

        self.toolButton_5 = QToolButton(self.verticalWidget)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_5.setStyleSheet(
            u"image: url(:/test/images/\u30c1\u30e3\u30c3\u30c8.png);")
        self.toolButton_5.setIconSize(QSize(88, 32))

        self.verticalLayout.addWidget(self.toolButton_5)

        self.toolButton_6 = QToolButton(self.verticalWidget)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_6.setStyleSheet(
            u"image: url(:/test/images/\u8ab2\u984c.png);")
        self.toolButton_6.setIconSize(QSize(88, 32))

        self.verticalLayout.addWidget(self.toolButton_6)

        self.toolButton_7 = QToolButton(self.verticalWidget)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_7.setStyleSheet(
            u"image: url(:/test/images/\u30c1\u30fc\u30e0.png);")
        self.toolButton_7.setIconSize(QSize(88, 32))

        self.verticalLayout.addWidget(self.toolButton_7)

        self.sidebutton5 = QPushButton(self.verticalWidget)
        self.sidebutton5.setObjectName(u"sidebutton5")
        self.sidebutton5.setCursor(QCursor(Qt.PointingHandCursor))
        self.sidebutton5.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                       "selection-background-color: rgb(53, 54, 95);\n"
                                       "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.sidebutton5)

        self.sidebutton6 = QPushButton(self.verticalWidget)
        self.sidebutton6.setObjectName(u"sidebutton6")
        self.sidebutton6.setCursor(QCursor(Qt.PointingHandCursor))
        self.sidebutton6.setStyleSheet(u"font: 13pt \".AppleSystemUIFont\";\n"
                                       "color : rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.sidebutton6)

        self.toolButton_9 = QToolButton(self.verticalWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_9.setStyleSheet(
            u"image: url(:/test/images/\u30d5\u30a1\u30a4\u30eb.png);")
        self.toolButton_9.setIconSize(QSize(88, 32))

        self.verticalLayout.addWidget(self.toolButton_9)

        self.toolButton_8 = QToolButton(self.verticalWidget)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_8.setStyleSheet(
            u"image: url(:/test/images/\u305d\u306e\u4ed6.png);")
        self.toolButton_8.setIconSize(QSize(88, 32))

        self.verticalLayout.addWidget(self.toolButton_8)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 851, 51))
        self.widget.setStyleSheet(u"background-color: rgb(53, 52, 98);")
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(270, 10, 371, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_10 = QLineEdit(self.widget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(200, 10, 16, 31))
        self.lineEdit_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_10.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);\n"
                                       "font: 14pt \".AppleSystemUIFont\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "gridline-color: rgba(255, 255, 255, 0);")
        self.lineEdit_10.setFrame(False)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_11 = QLineEdit(self.widget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(230, 10, 21, 31))
        self.lineEdit_11.setStyleSheet(u"font: 14pt \".AppleSystemUIFont\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "color: rgb(94, 94, 129);")
        self.lineEdit_11.setFrame(False)
        self.lineEdit_11.setReadOnly(True)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(520, 40, 851, 51))
        self.widget_4.setStyleSheet(u"background-color: rgb(53, 52, 98);")
        self.textEdit_2 = QTextEdit(self.widget_4)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(270, 10, 371, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(122, 121, 149);")
        self.lineEdit_15 = QLineEdit(self.widget_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(180, 10, 41, 41))
        self.lineEdit_15.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);\n"
                                       "font: 14pt \".AppleSystemUIFont\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "gridline-color: rgba(255, 255, 255, 0);")
        self.lineEdit_16 = QLineEdit(self.widget_4)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(220, 10, 41, 41))
        self.lineEdit_16.setStyleSheet(u"font: 14pt \".AppleSystemUIFont\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "gridline-color: rgba(255, 255, 255, 0);\n"
                                       "border-top-color: rgb(40, 35, 82);")
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 20, 21, 21))
        self.radioButton.setStyleSheet(u"")
        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(30, 20, 21, 21))
        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(50, 20, 21, 21))
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(270, 50, 581, 51))
        self.widget_3.setStyleSheet(u"background-color: rgb(240, 239, 238);")
        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 10, 81, 31))
        self.lineEdit_2.setStyleSheet(u"font: 14pt \".AppleSystemUIFont\";")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(140, 10, 61, 31))
        self.lineEdit_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(200, 10, 61, 31))
        self.lineEdit_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8 = QLineEdit(self.widget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(260, 10, 21, 31))
        self.lineEdit_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_8.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";")
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setReadOnly(True)
        self.toolButton_2 = QToolButton(self.widget_3)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(380, 10, 31, 31))
        self.toolButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet(u"image: url(:/test/images/camera.svg);\n"
                                        "background-color: rgb(79, 78, 150);")
        self.toolButton_3 = QToolButton(self.widget_3)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(420, 10, 31, 31))
        self.toolButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_3.setStyleSheet(u"image: url(:/test/images/call.svg);\n"
                                        "background-color: rgb(79, 78, 150);")
        self.toolButton_4 = QToolButton(self.widget_3)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(460, 10, 31, 31))
        self.toolButton_4.setStyleSheet(u"image: url(:/test/images/download.svg);\n"
                                        "background-color: rgb(79, 78, 150);")
        self.toolButton_10 = QToolButton(self.widget_3)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setGeometry(QRect(10, 10, 31, 31))
        self.toolButton_10.setStyleSheet(
            u"image: url(:/test/images/icon.png);")
        self.toolButton_10.setIconSize(QSize(88, 32))
        self.toolButton_12 = QToolButton(self.widget_3)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setGeometry(QRect(500, 10, 31, 31))
        self.toolButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_12.setStyleSheet(u"image: url(:/test/images/attend_plus.svg);\n"
                                         "background-color: rgb(240, 239, 238);\n"
                                         "")
        self.toolButton_13 = QToolButton(self.widget_3)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setGeometry(QRect(540, 10, 31, 31))
        self.toolButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_13.setStyleSheet(u"image: url(:/test/images/popup.svg);\n"
                                         "background-color: rgb(240, 239, 238);\n"
                                         "")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(80, 50, 191, 151))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(self.widget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 10, 71, 41))
        self.lineEdit_5.setStyleSheet(u"border: solid;\n"
                                      "font: 18pt \".AppleSystemUIFont\";")
        self.lineEdit_5.setInputMask(u"")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6 = QLineEdit(self.widget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(90, 10, 41, 41))
        self.lineEdit_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_6.setStyleSheet(u"color: rgb(79, 78, 150);\n"
                                      "border-bottom-color: rgb(67, 59, 140);\n"
                                      "font: 13pt \".AppleSystemUIFont\";")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_14 = QLineEdit(self.widget_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(130, 10, 51, 41))
        self.lineEdit_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_14.setFrame(False)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 60, 113, 21))
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 60, 51, 32))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.toolButton_11 = QToolButton(self.widget_2)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setGeometry(QRect(10, 100, 91, 31))
        self.toolButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_11.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(270, 100, 581, 471))
        self.scrollArea.setMinimumSize(QSize(581, 471))
        self.scrollArea.setStyleSheet(u"border: solid;")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 581, 471))
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 581, 471))
        self.widget_5.setStyleSheet(u"background-color: rgb(240, 239, 238);")
        self.textEdit_5 = QTextEdit(self.widget_5)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(40, 270, 211, 81))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                      "border: solid;")
        self.textEdit_5.setReadOnly(True)
        self.textEdit_6 = QTextEdit(self.widget_5)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(340, 200, 221, 61))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(223, 222, 238);\n"
                                      "border: solid;")
        self.textEdit_6.setReadOnly(True)
        self.textEdit_7 = QTextEdit(self.widget_5)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(40, 90, 211, 71))
        self.textEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                      "border: solid;")
        self.textEdit_7.setReadOnly(True)
        self.textEdit_8 = QTextEdit(self.widget_5)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(340, 10, 221, 71))
        self.textEdit_8.setStyleSheet(u"background-color: rgb(223, 222, 238);\n"
                                      "border: solid;")
        self.textEdit_8.setReadOnly(True)
        self.lineEdit_9 = QLineEdit(self.widget_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(260, 170, 51, 21))
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setReadOnly(True)
        self.textEdit_9 = QTextEdit(self.widget_5)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(110, 370, 371, 31))
        self.textEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 429, 81, 101))
        self.widget_6.setStyleSheet(u"background-color: rgb(35, 36, 53);")
        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(79, 49, 771, 481))
        self.widget_7.setStyleSheet(
            u"background-color: rgba(55, 55, 56, 128);")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(550, 90, 31, 31))
        self.widget_8.setStyleSheet(u"image: url(:/test/images/x.svg);\n"
                                    "background-color: rgb(255, 255, 255);")
        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(190, 100, 381, 301))
        self.widget_9.setStyleSheet(u"background-color: rgb(240, 239, 238);")
        self.toolButton_14 = QToolButton(self.widget_9)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setGeometry(QRect(110, 230, 151, 41))
        self.toolButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(79, 78, 150);\n"
                                         "font: 24pt \".AppleSystemUIFont\";")
        self.textEdit_4 = QTextEdit(self.widget_9)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(20, 140, 341, 61))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textEdit_3 = QTextEdit(self.widget_9)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(20, 50, 341, 61))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_9.raise_()
        self.widget_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.listWidget, self.sidebutton5)
        QWidget.setTabOrder(self.sidebutton5, self.sidebutton6)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.pushButton.showMenu)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate(
            "MainWindow", u"\u3060\u3093\u30543\u5144\u5f1f", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate(
            "MainWindow", u"\u3060\u3093\u30544\u5144\u5f1f", None))
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate(
            "MainWindow", u"\u304a\u3088\u3052\u305f\u3044\u3084\u304d\u304f\u3093", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.toolButton.setText("")
        self.toolButton_5.setText("")
        self.toolButton_6.setText("")
        self.toolButton_7.setText("")
# if QT_CONFIG(whatsthis)
        self.sidebutton5.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sidebutton5.setText(QCoreApplication.translate(
            "MainWindow", u"\u4e88\u5b9a\u8868", None))
        self.sidebutton6.setText(QCoreApplication.translate(
            "MainWindow", u"\u901a\u8a71", None))
        self.toolButton_9.setText("")
        self.toolButton_8.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#363550;\">\u4eba\u3001\u30ad\u30fc\u30ef\u30fc\u30c9\u306e\u691c\u7d22\u3001\u307e\u305f\u306f\u30b3\u30de\u30f3\u30c9\u306e\u5165\u529b</span></p></body></html>", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_10.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                               "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_10.setText(
            QCoreApplication.translate("MainWindow", u"<", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_11.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                               "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_11.setText(
            QCoreApplication.translate("MainWindow", u">", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#363550;\">\u4eba\u3001\u30ad\u30fc\u30ef\u30fc\u30c9\u306e\u691c\u7d22\u3001\u307e\u305f\u306f\u30b3\u30de\u30f3\u30c9\u306e\u5165\u529b</span></p></body></html>", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_15.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                               "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_15.setText(
            QCoreApplication.translate("MainWindow", u"<", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_16.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                               "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_16.setText(
            QCoreApplication.translate("MainWindow", u">", None))
        self.radioButton.setText("")
        self.radioButton_2.setText("")
        self.radioButton_3.setText("")
# if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                              "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u3060\u3093\u30543\u5144\u5f1f", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_4.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                              "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u30c1\u30e3\u30c3\u30c8", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_7.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                              "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_7.setText(QCoreApplication.translate(
            "MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_8.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                              "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_8.setText(
            QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_2.setText("")
        self.toolButton_3.setText("")
        self.toolButton_4.setText("")
        self.toolButton_10.setText("")
        self.toolButton_12.setText("")
        self.toolButton_13.setText("")
# if QT_CONFIG(tooltip)
        self.lineEdit_5.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                              "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u30c1\u30e3\u30c3\u30c8", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_6.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                              "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_6.setText(QCoreApplication.translate(
            "MainWindow", u"\u6700\u8fd1", None))
# if QT_CONFIG(tooltip)
        self.lineEdit_14.setToolTip(QCoreApplication.translate("MainWindow", u"def change_value(self):\n"
                                                               "        self.text = \"yattaze\"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_14.setText(QCoreApplication.translate(
            "MainWindow", u"\u9023\u7d61\u5148", None))
        self.lineEdit.setText(QCoreApplication.translate(
            "MainWindow", u"\u691c\u7d22\u6b04", None))
        self.pushButton.setText("")
        self.toolButton_11.setText(QCoreApplication.translate(
            "MainWindow", u"+ \u65b0\u898f\u4f5c\u6210", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#343434;\">\u517c\u5cf6 \u5149\u5e73</span><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:14px; color:#343434;\"> </span><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#8f8f8f;\">17:21</span></p>\n"
                                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block"
                                                           "-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:14px;\">\u3042\u3042\uff5e\u3044\u3044\u3063\u3059\u306d\uff5e</span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#7a7a7a;\">16:49</span></p>\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:14px;\">\u3042\u3001push\u3067\u304d\u305f\u3067</span></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#343434;\">\u517c\u5cf6 \u5149\u5e73 </span><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#7c7c7c;\">\u6628\u65e5</span><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#8f8f8f;\">17:44</span></p>\n"
                                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0p"
                                                           "x; -qt-block-indent:0; text-indent:0px;\">\u306a\u3093\u3067\u6012\u3089\u308c\u3068\u3093</p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI','system-ui','Apple Color Emoji','Segoe UI Emoji','sans-serif'; font-size:12pt; color:#7a7a7a;\">\u6628\u65e517:31</span></p>\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u306a\u3093\u304bGIthub\u306bpush\u3067\u304d\u306d\u3047\u3002\u3002\u3002</p></body></html>", None))
        self.lineEdit_9.setText(QCoreApplication.translate(
            "MainWindow", u"\u4eca\u65e5", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#373534;\">\u65b0\u3057\u3044\u30e1\u30c3\u30bb\u30fc\u30b8\u306e\u5165\u529b</span></p></body></html>", None))
        self.toolButton_14.setText(QCoreApplication.translate(
            "MainWindow", u"\u4f5c\u6210", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u30b0\u30eb\u30fc\u30d7\u540d </span></p>\n"
                                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u203b\u62db\u5f85\u3059\u308b\u30e1\u30f3\u30d0\u30fc\u304c2\u540d\u4ee5\u4e0a\u306e\u307f</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">\u62db\u5f85\u3059\u308b\u30e1\u30f3\u30d0\u30fc</span></p></body></html>", None))
    # retranslateUi

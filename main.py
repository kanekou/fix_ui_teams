# -*- coding: utf-8 -*-
import sys
from chat_screen import Ui_MainWindow  # pythonへ変換したuiファイルを読み込む
from chat_screen_new_chat import Ui_MainWindow2  # pythonへ変換したuiファイルを読み込む
import chat_screen_rcc
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    # Ui_MainWindow生成のための初期化処理
    def __init__(self, parent=None):

        # UI初期化処理
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class MainWindow2(QMainWindow):
    # Ui_MainWindow生成のための初期化処理
    def __init__(self, parent=None):
        # UI初期化処理
        super(MainWindow2, self).__init__()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)

    # Ui_MainWindow2().toolButton_11.clicked.connect(changeView)


def changeViewToNewChat():  # chat_screen   -> chat_screen_new_chat に遷移させる
    window.hide()  # chat_screen を hide
    window2.show()  # chat_screen_new_chat を show


def changeViewToChatScreen():  # chat_screen   -> chat_screen_new_chat に遷移させる
    window2.hide()  # chat_screen を hide
    window.show()  # chat_screen_new_chat を show


# 実行処理
if __name__ == "__main__":
    # アプリケーション作成
    app = QApplication(sys.argv)
    # オブジェクト作成
    window = MainWindow()  # chat_screen
    window2 = MainWindow2()  # chat_screen_new_chat
    # MainWindowの表示
    window.show()
    window.ui.toolButton_11.clicked.connect(changeViewToNewChat)
    window2.ui2.toolButton_14.clicked.connect(changeViewToChatScreen)

    sys.exit(app.exec_())

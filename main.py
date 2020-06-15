# -*- coding: utf-8 -*-
import sys
from chat_screen import Ui_MainWindow #pythonへ変換したuiファイルを読み込む
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    #Ui_MainWindow生成のための初期化処理
    def __init__(self, parent = None):

        #UI初期化処理
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#実行処理
if __name__=="__main__":
    #アプリケーション作成
    app = QApplication(sys.argv)
    #オブジェクト作成
    window = MainWindow()
    #MainWindowの表示
    window.show()
    sys.exit(app.exec_())

import sys
import os.path

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

class ItemView(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(ItemView, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout(self)

        self.__filter = QtWidgets.QLineEdit(self)
        self.__filter.textChanged.connect(self.filterChanged)
        layout.addWidget(self.__filter)

        self.__listView = QtWidgets.QListView(self)

        # self.proxymodel = TestProxyFilter(
        # self.__listView.setModel(self.proxyModel)
        layout.addWidget(self.__listView)

        def setSourceModel(self, model):
            self.__proxyModel.setSourceModel(model)

    def filterChanged(self, regText):
        regExp = QtCore.QRegExp(
            regText,
            QtCore.Qt.CaseSensitive,
            QtCore.QRegExp.Wildcard
        )
        self.proxymodel.setFilterRegExp(regExp)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = ItemView()
    a.show()
    sys.exit(app.exec_())

#!python3
# -*- coding: utf-8 -*-

import sys
import os.path

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

PROXY_FILTER_ROLE = QtCore.Qt.UserRole + 1


class BaseItem(object):
    def __init__(self, data=None, parent=None):

        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return 1

    def data(self, column):
        if self.itemData is None:
            return ""
        return self.itemData['key']

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0

    def clear(self):
        self.childItems = []


class TreeItem(BaseItem):

    def __init__(self, data, parent=None):
        super(TreeItem, self).__init__(data=data, parent=parent)


class GroupItem(BaseItem):

    def __init__(self, groupName, parent=None):
        super(GroupItem, self).__init__(data=[], parent=parent)

        self.groupName = groupName

    def data(self, column):

        return self.groupName


class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, items=[], parent=None):
        super(TreeModel, self).__init__(parent)

        self.__items = items
        self.rootItem = BaseItem()

        self.setItems(items)

    def setItems(self, items):

        self.__items = items
        self.setupModelData()

    def addItem(self, item):

        self.__items.append(item)
        self.setupModelData()

    def columnCount(self, parent):

        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role=QtCore.Qt.DisplayRole):

        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole:
            return item.data(index.column())
        # ProxyModelを使用した検索時の検索対象文字列を返す
        if role == PROXY_FILTER_ROLE:
            # とりあえず同じものを返す
            return item.data(index.column())
        return None

    def flags(self, index):

        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)
        return None

    def index(self, row, column, parent):

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):

        if not index.isValid():
            return QtCore.QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.rootItem:
            return QtCore.QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):

        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
        return parentItem.childCount()

    def setupModelData(self):
        """
        表示用のItemを再構築する
        """
        self.rootItem.clear()
        parents = {}
        for item in self.__items:
            if item['parent'] in parents:
                p = parents[item['parent']]
            else:
                p = GroupItem(item['parent'], self.rootItem)
                self.rootItem.appendChild(p)
                parents[item['parent']] = p
            treeItem = TreeItem(item, p)
            p.appendChild(treeItem)
        self.layoutChanged.emit()


class UISample(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(UISample, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        # カスタムUIを作成
        self.list = QtWidgets.QTreeView()
        layout.addWidget(self.list)

        self.search = QtWidgets.QLineEdit(self)
        layout.addWidget(self.search)

        # てきとうにListに表示するItemの配列を作る
        data = []
        data.append({'parent': 'GroupA', 'key': 'hogehogeItem'})
        data.append({'parent': 'GroupA', 'key': 'テスト'})
        data.append({'parent': 'GroupA', 'key': 'GroupAのアイテム'})
        data.append({'parent': 'GroupB', 'key': 'GroupBのアイテム'})
        data.append({'parent': 'GroupB', 'key': 'GroupBのほげほげ'})
        data.append({'parent': 'GroupB', 'key': 'GroupBのテスト'})

        self.model = TreeModel(data)
        self.proxymodel = TestProxyFilter()
        self.proxymodel.setSourceModel((self.model))
        self.proxymodel.setFilterRole(PROXY_FILTER_ROLE)
        self.list.setModel(self.proxymodel)
        self.search.textChanged.connect(self.filterChanged)
        # 全部開いておく
        self.list.expandAll()

        self.setLayout(layout)

    def filterChanged(self, regText):

        regExp = QtCore.QRegExp(
            regText,
            QtCore.Qt.CaseSensitive,
            QtCore.QRegExp.Wildcard
        )
        self.proxymodel.setFilterRegExp(regExp)


class TestProxyFilter(QtCore.QSortFilterProxyModel):

    def __init__(self, parent=None):
        super(TestProxyFilter, self).__init__(parent)

    def filterAcceptsRow(self, row, parent):
        item = parent.internalPointer()
        # 親ItemがGroupItemは、ProxyModelの検索対象にする
        if isinstance(item, GroupItem):
            return super(TestProxyFilter, self).filterAcceptsRow(row, parent)
        # それ以外は検索で消えてほしくないのでTrueにする
        return True


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = UISample()
    a.show()
    sys.exit(app.exec_())

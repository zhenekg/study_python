#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import gui
from mysqlConnect import ats, efw

class Prog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currentList = []
        self.menu_item_ats.triggered.connect(self.atsView)
        self.menu_item_gates.triggered.connect(self.efwView)
        self.listWidget.itemClicked.connect(self.listSelectItem)

    def atsView(self):
        self.currentList = ats
        self.listWidget.clear()
        for item in self.currentList:
            self.listWidget.addItem(item.getName())

    def efwView(self):
        self.currentList = efw
        self.listWidget.clear()
        for item in self.currentList:
            self.listWidget.addItem(item.getName())

    def listSelectItem(self):
        self.label_view.setText(self.currentList[self.listWidget.currentRow()].getAddress())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Prog()
    form.show()
    sys.exit(app.exec_())

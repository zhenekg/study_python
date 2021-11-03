#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QThread
from mysqlConnect import ats, efw

class Prog(QWidget):
    def __init__(self):
        super().__init__()
        self.set()
        self.currentList = []
        self.w_root.btn_ats.clicked.connect(self.atsView)
        self.w_root.btn_gw.clicked.connect(self.efwView)
        self.w_root.listWidget.itemClicked.connect(self.listSelectItem)

    def set(self):
        self.w_root = uic.loadUi('gui2.ui')
        self.w_root.show()

    def atsView(self):
        self.currentList = ats
        self.w_root.listWidget.clear()
        for item in self.currentList:
            self.w_root.listWidget.addItem(item.getName())

    def efwView(self):
        self.currentList = efw
        self.w_root.listWidget.clear()
        for item in self.currentList:
            self.w_root.listWidget.addItem(item.getName())

    def listSelectItem(self):
        self.w_root.label_ip.setText(self.currentList[self.w_root.listWidget.currentRow()].getAddress())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Prog()
    app.exec_()

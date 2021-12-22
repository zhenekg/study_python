#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QThread
from mysqlConnect import ats, efw

W_SHOW = [
    170, 171, 172, 173, 175, 178, 181, 202, 236, 291, 380, 524, 757, 800
]

W_HIDE = [
   170, 192, 425, 569, 658, 713, 747, 768, 781, 789, 794, 797, 799, 800
]


class ConnectData(QThread):
    print("Hello!!!!")

    def __init__(self):
        super(self).__init__()





class Prog(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.set()
        self.currentList = []
        self.show_more = True
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
        self.setWidth()

    def efwView(self):
        self.currentList = efw
        self.w_root.listWidget.clear()
        for item in self.currentList:
            self.w_root.listWidget.addItem(item.getName())
        self.setWidth()

    def listSelectItem(self):
        self.w_root.label_ip.setText(self.currentList[self.w_root.listWidget.currentRow()].getAddress())

    def setWidth(self):
        if self.show_more:
            for i in W_SHOW:
                self.w_root.resize(i, 600)
                self.app.processEvents()
                time.sleep(.02)
        self.show_more = False
        Prog.show_more = self.show_more


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Prog(app)
    app.exec_()

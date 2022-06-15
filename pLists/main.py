#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import gui


class App(QMainWindow, gui.Ui_pLists):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.menu_exit.triggered.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()

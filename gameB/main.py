#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import gui


class App(QMainWindow, gui.Ui_Game_B):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()

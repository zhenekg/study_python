#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread
import gui


class Resinfo(QThread):
    res_memmory = 100
    res_cpu = 100

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try:
                self.res_memmory
            except:
                self.res_memmory = 100
            print('thread')
            time.sleep(3)


class App(QWidget, gui.Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        resinfo = Resinfo()
        resinfo.start()
        self.setupUi(self)
        self.pixmap = QPixmap("1.jpg")
        self.pixmap2 = QPixmap("2.jpg")
        self.label.setPixmap(self.pixmap)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import time
import psutil
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QTimer
import gui


class Resinfo(QThread):
    res_cpu = 100
    res_memmory = 100

    def __init__(self):
        QThread.__init__(self)
        dict(psutil.virtual_memory()._asdict())
        self.res_memmory = psutil.virtual_memory().percent
        self.res_cpu = psutil.cpu_percent()

    def run(self):
        while True:

           # print(self.res_cpu)
           # print(self.res_memmory)
            time.sleep(3)


class App(QWidget, gui.Ui_Form):

    def __init__(self):
        QWidget.__init__(self)


        self.pixmap1 = QPixmap("arika0_20.png")
        self.pixmap2 = QPixmap("arika21_40.png")
        self.pixmap3 = QPixmap("arika41_60.png")
        self.pixmap4 = QPixmap("arika61_80.png")
        self.pixmap5 = QPixmap("arika81_90.png")
        self.pixmap6 = QPixmap("arika91_100.png")
        self.setupUi(self)
        self.setData()
        self.timer = QTimer()
        self.timer.timeout.connect(self.setData)
        self.timer.start(2000)


    def setData(self):
        self.resinfo = Resinfo()
        self.resinfo.start()
        self.cpu_data = self.resinfo.res_cpu
        self.label_cpu.setText(str(self.cpu_data) + "%")
        if 0 < self.cpu_data <= 20:
            self.pixmap_view = self.pixmap1
        elif 20 < self.cpu_data <= 40:
            self.pixmap_view = self.pixmap2
        elif 40 < self.cpu_data <= 60:
            self.pixmap_view = self.pixmap3
        elif 60 < self.cpu_data <= 80:
            self.pixmap_view = self.pixmap4
        elif 80 < self.cpu_data <= 90:
            self.pixmap_view = self.pixmap5
        elif 90 <self.cpu_data <= 100:
            self.pixmap_view = self.pixmap6

        self.label.setPixmap(self.pixmap_view)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()
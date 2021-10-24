#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtCore, QtTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread
import weather
import datetime
import time
from weather import DAYS


class WeatherData(QThread):
    req = weather.today()
    city = req['city']
    temp = req['temp']

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            try:
                req = weather.today()
            except:
                req['city'] = self.city
                req['temp'] = self.temp
            print('thread')
            time.sleep(3)


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.weather = WeatherData()
        self.weather.start()
        self.set()

    def set(self):
        self.w_root = uic.loadUi('gui.ui')
        self.w_root.btn_slice.clicked.connect(self.setHeight)
        self.w_root.show()

    def setHeight(self):
        print("dsadada")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()

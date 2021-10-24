#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtTest
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QTimer
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
    tic = False
    def __init__(self):
        QWidget.__init__(self)
        self.weather = WeatherData()
        self.weather.start()
        self.set()
        self.setData()
        self.timer = QTimer()
        self.timer.timeout.connect(self.setData)
        self.timer.start(1000)


    def set(self):
        self.w_root = uic.loadUi('gui.ui')
        self.w_root.btn_slice.clicked.connect(self.setHeight)
        self.w_root.show()

    def setData(self):
        self.w_root.label_temp.setText(str(self.weather.temp) + " °C")
        self.w_root.label_city.setText(self.weather.city)
        # Time
        if self.tic:
            now = datetime.datetime.today().strftime("%H:%M:%S")
            self.tic = False
        else:
            now = datetime.datetime.today().strftime("%H %M %S")
            self.tic = True
        self.w_root.label_time.setText(now)

    def setHeight(self):
        print("dsadada")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()

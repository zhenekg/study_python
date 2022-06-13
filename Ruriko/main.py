#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import QThread, QTimer
import gui


class App(QMainWindow, gui.Ui_Ruriko):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Body
        self.body = os.listdir("src/img/body/")
        for item in self.body:
            self.comboBox_body.addItem(item[:-4])
        # Hair
        self.hair = os.listdir("src/img/hair")
        for item in self.hair:
            self.comboBox_hair.addItem(item[:-4])
        # Face
        self.face = os.listdir("src/img/face/")
        for item in self.face:
            self.comboBox_face.addItem(item[:-4])
        # Pubic
        self.pubic = os.listdir("src/img/pubic/")
        for item in self.pubic:
            self.comboBox_pubic.addItem(item[:-4])
        # Piercing
        self.piercing = os.listdir("src/img/piercing/")
        for item in self.piercing:
            self.comboBox_piercing.addItem(item[:-4])
        # Panty
        self.panty = os.listdir("src/img/panty/")
        for item in self.panty:
            self.comboBox_panty.addItem(item[:-4])
        # Bra
        self.bra = os.listdir("src/img/bra/")
        for item in self.bra:
            self.comboBox_bra.addItem(item[:-4])
        # Legs
        self.legs = os.listdir("src/img/legs/")
        for item in self.legs:
            self.comboBox_legs.addItem(item[:-4])
        # Shoes
        self.shoes = os.listdir("src/img/shoes/")
        for item in self.shoes:
            self.comboBox_shoes.addItem(item[:-4])
        # Top
        self.top = os.listdir("src/img/top/")
        for item in self.top:
            self.comboBox_top.addItem(item[:-4])
        # Bottom
        self.bottom = os.listdir("src/img/bottom/")
        for item in self.bottom:
            self.comboBox_bottom.addItem(item[:-4])
        # Dress
        self.dress = os.listdir("src/img/dress/")
        for item in self.dress:
            self.comboBox_dress.addItem(item[:-4])
        # Accesuars
        self.acc = os.listdir("src/img/acc/")
        for item in self.acc:
            self.comboBox_acc.addItem(item[:-4])
        # self.pixmap_14
        # Full
        self.full = os.listdir("src/img/full/")
        for item in self.full:
            self.comboBox_full.addItem(item[:-4])

        self.label_body.setScaledContents(True)
        self.label_hair.setScaledContents(True)
        self.label_face.setScaledContents(True)
        self.label_pubic.setScaledContents(True)
        self.label_piercing.setScaledContents(True)
        self.label_panty.setScaledContents(True)
        self.label_bra.setScaledContents(True)
        self.label_legs.setScaledContents(True)
        self.label_shoes.setScaledContents(True)
        self.label_top.setScaledContents(True)
        self.label_bottom.setScaledContents(True)
        self.label_dress.setScaledContents(True)
        self.label_acc.setScaledContents(True)
        self.label_14.setScaledContents(True)
        self.label_full.setScaledContents(True)

        self.set_default()
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.setData)
        # self.timer.start(2000)
        self.pushButton_nude.clicked.connect(self.set_nude)
        self.pushButton_default.clicked.connect(self.set_default)
        self.comboBox_body.currentIndexChanged.connect(self.set_data)
        self.comboBox_hair.currentIndexChanged.connect(self.set_data)
        self.comboBox_face.currentIndexChanged.connect(self.set_data)
        self.comboBox_pubic.currentIndexChanged.connect(self.set_data)
        self.comboBox_piercing.currentIndexChanged.connect(self.set_data)
        self.comboBox_panty.currentIndexChanged.connect(self.set_data)
        self.comboBox_bra.currentIndexChanged.connect(self.set_data)
        self.comboBox_legs.currentIndexChanged.connect(self.set_data)
        self.comboBox_shoes.currentIndexChanged.connect(self.set_data)
        self.comboBox_top.currentIndexChanged.connect(self.set_data)
        self.comboBox_bottom.currentIndexChanged.connect(self.set_data)
        self.comboBox_dress.currentIndexChanged.connect(self.set_dress)
        self.comboBox_acc.currentIndexChanged.connect(self.set_data)
        self.comboBox_full.currentIndexChanged.connect(self.set_data)
    def set_dress(self):
        self.comboBox_bottom.setCurrentText("none")
        self.set_data()

    def set_draw(self):
        self.label_body.setPixmap(self.pixmap_body)
        self.label_hair.setPixmap(self.pixmap_hair)
        self.label_face.setPixmap(self.pixmap_face)
        self.label_pubic.setPixmap(self.pixmap_pubic)
        self.label_piercing.setPixmap(self.pixmap_piercing)
        self.label_panty.setPixmap(self.pixmap_panty)
        self.label_bra.setPixmap(self.pixmap_bra)
        self.label_legs.setPixmap(self.pixmap_legs)
        self.label_shoes.setPixmap(self.pixmap_shoes)
        self.label_top.setPixmap(self.pixmap_top)
        self.label_bottom.setPixmap(self.pixmap_bottom)
        self.label_dress.setPixmap(self.pixmap_dress)
        self.label_acc.setPixmap(self.pixmap_acc)
        self.label_full.setPixmap(self.pixmap_full)

    def set_data(self):
        self.pixmap_body = QPixmap("src/img/body/"+self.comboBox_body.currentText()+".png")
        self.pixmap_hair = QPixmap("src/img/hair/"+self.comboBox_hair.currentText()+".png")
        self.pixmap_face = QPixmap("src/img/face/"+self.comboBox_face.currentText()+".png")
        self.pixmap_pubic = QPixmap("src/img/pubic/"+self.comboBox_pubic.currentText()+".png")
        self.pixmap_piercing = QPixmap("src/img/piercing/"+self.comboBox_piercing.currentText()+".png")
        self.pixmap_panty = QPixmap("src/img/panty/"+self.comboBox_panty.currentText()+".png")
        self.pixmap_bra = QPixmap("src/img/bra/"+self.comboBox_bra.currentText()+".png")
        self.pixmap_legs = QPixmap("src/img/legs/"+self.comboBox_legs.currentText()+".png")
        self.pixmap_shoes = QPixmap("src/img/shoes/"+self.comboBox_shoes.currentText()+".png")
        self.pixmap_top = QPixmap("src/img/top/"+self.comboBox_top.currentText()+".png")
        self.pixmap_bottom = QPixmap("src/img/bottom/"+self.comboBox_bottom.currentText()+".png")
        self.pixmap_dress = QPixmap("src/img/dress/"+self.comboBox_dress.currentText()+".png")
        self.pixmap_acc = QPixmap("src/img/acc/" + self.comboBox_acc.currentText() + ".png")
        self.pixmap_full = QPixmap("src/img/full/" + self.comboBox_full.currentText() + ".png")
        self.set_draw()

    def set_default(self):
        self.comboBox_body.setCurrentText("default")
        self.comboBox_hair.setCurrentText("Brunette")
        self.comboBox_face.setCurrentText("Smile")
        # self.comboBox_pubic.setCurrentText("none")
        self.comboBox_piercing.setCurrentText("none")
        self.comboBox_panty.setCurrentText("White")
        self.comboBox_bra.setCurrentText("none")
        self.comboBox_legs.setCurrentText("Stockins white")
        self.comboBox_shoes.setCurrentText("School")
        self.comboBox_top.setCurrentText("School")
        self.comboBox_bottom.setCurrentText("School")
        self.comboBox_dress.setCurrentText("none")
        self.comboBox_acc.setCurrentText("none")
        self.comboBox_full.setCurrentText("none")
        self.set_data()

    def set_nude(self):
        self.comboBox_body.setCurrentText("none")
        self.comboBox_hair.setCurrentText("none")
        self.comboBox_face.setCurrentText("none")
        # self.comboBox_pubic.setCurrentText("none")
        self.comboBox_piercing.setCurrentText("none")
        self.comboBox_panty.setCurrentText("none")
        self.comboBox_bra.setCurrentText("none")
        self.comboBox_legs.setCurrentText("none")
        self.comboBox_shoes.setCurrentText("none")
        self.comboBox_top.setCurrentText("none")
        self.comboBox_bottom.setCurrentText("none")
        self.comboBox_dress.setCurrentText("none")
        self.comboBox_acc.setCurrentText("none")
        self.comboBox_full.setCurrentText("none")
        self.set_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()

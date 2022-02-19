#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QTimer
import gui


class App(QWidget, gui.Ui_Ruriko):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pixmap = QPixmap("src/img/RurikoBody.png")
        self.pixmapHair = QPixmap("src/img/RurikoBlond.png")
        self.pixmapFace = QPixmap("src/img/RurikoFace.png")
        self.pixmapUpper = QPixmap("src/img/RurikoSchoolUniform.png")
        self.label.setPixmap(self.pixmap)
        self.labelHair.setPixmap(self.pixmapHair)
        self.labelFace.setPixmap(self.pixmapFace)
        self.labelUpper.setPixmap(self.pixmapUpper)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()
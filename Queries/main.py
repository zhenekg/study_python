#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from datetime import date
import os
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import QThread, QTimer
import gui
import gui1
import basesql


class QueryNew(QDialog, gui1.Ui_Dialog):
    def __init__(self,):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pixmap = QPixmap()
        self.pixmap = 0
        self.button_cancel.clicked.connect(self.cans_btn)
        self.button_send.clicked.connect(self.send_btn)
        self.button_screen.clicked.connect(self.add_screen_btn)

    def cans_btn(self):
        self.close()

    def send_btn(self):
        self.theme = self.line_edit_theme.text()
        self.description = self.text_edit_description.toPlainText()
        self.status = "открыта"
        self.screen = self.pixmap
        write_in = basesql.SQLconnection()
        write_in.write_base("открыта", "ИТ", self.line_edit_theme.text(), self.text_edit_description.toPlainText(), "user", "Горбатенко", 0)
        self.close()

    def add_screen_btn(self):
        self.close()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])


class App(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.data = basesql.SQLconnection()
        self.rows = self.data.read_base()
        self.model = TableModel(self.rows)
        self.query_view = QueryNew()
        self.set_data()
        self.button_new.clicked.connect(self.query_new)

    def set_data(self):
        self.label_data.setText(str(date.today().strftime('%d %b %Y')))
        self.tableView.setModel(self.model)

    def query_new(self):
        self.close()
        self.query_view.show()

    def query_refresh(self):
        self.set_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()

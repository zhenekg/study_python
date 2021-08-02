import sys

from PyQt5.QtGui import QTextCharFormat

import gui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from server import ServerSocket
from client import ClientSocket
from PyQt5.QtCore import QThread, Qt


class ServerThread(QThread):
    def __init__(self):
        super(ServerThread, self).__init__()

    def run(self):
        s = ServerSocket()
        s.server_start()


class Prog(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.thread_server = ServerThread()
        self.dict_for_sent = {}
        self.setupUi(self)
        self.pushButton_server_start.clicked.connect(self.start_server)
        self.pushButton_file_open.clicked.connect(self.open_file)
        self.pushButton_find.clicked.connect(self.find_in_text)
        self.pushButton_detail.clicked.connect(self.detail_info)

    def start_server(self):
        self.thread_server.start()
        c = ClientSocket()
        self.label_status_connect.setText(c.client_send("status"))
        self.pushButton_file_open.setEnabled(True)

    def open_file(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.label_filename.setText(path)
        text = open(path, "r")
        data = text.read()
        self.textEdit.setText(data)
        self.dict_for_sent['text'] = data
        text.close()
        self.lineEdit_find.setEnabled(True)
        self.pushButton_find.setEnabled(True)

    def find_in_text(self):
        self.dict_for_sent['mask'] = self.lineEdit_find.text()
        self.textEdit.setEnabled(True)
        self.pushButton_detail.setEnabled(True)
        self.on_find(self.lineEdit_find.text())

    def on_find(self, rx):
        fmt = QTextCharFormat()
        fmt.setBackground(Qt.blue)
        cursor = self.textEdit.document().find(rx, 0)
        cursor.mergeCharFormat(fmt)
        while not cursor.isNull():
            pos = cursor.position()
            cursor = self.textEdit.document().find(rx, pos)
            cursor.mergeCharFormat(fmt)

    def detail_info(self):
        c = ClientSocket()
        self.label_find.setText(c.client_send(self.dict_for_sent))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Prog()
    form.show()
    sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import gui
import os


class RenameFiles(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_to_dir = ''
        self.button_path_to_dir.clicked.connect(self.choose_folder)
        self.button_ok.clicked.connect(self.rename_exts)

    def choose_folder(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.path_to_dir = dir + "/"
        self.label.setText(self.path_to_dir)

    def rename_exts(self):
        for filename in os.listdir(self.path_to_dir):
            os.rename(filename, filename+self.line_edit_dst)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RenameFiles()
    form.show()
    sys.exit(app.exec_())
# Test
import sys
from PyQt5.QtWidgets import *

import gui
from answer import Choice, questions, statuses


class Prog(QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = -1
        self.answers = []
        for i in range(0, len(questions)):
            self.answers.append(Choice(questions[i], 0))
        self.pushButtonNext.clicked.connect(self.pushButtonNextClicked)
        self.pushButtonPrev.clicked.connect(self.pushButtonPrevClicked)
        self.radioButton_1.toggled.connect(self.rb1Checked)
        self.radioButton_2.toggled.connect(self.rb2Checked)
        self.radioButton_3.toggled.connect(self.rb3Checked)
        self.radioButton_4.toggled.connect(self.rb4Checked)
        self.label.setText("Нужно ответить на все вопросы, выбрав одно из 4-х значений")

    def rb1Checked(self):
        self.pushButtonNext.setEnabled(True)
        self.answers[self.count].setAnswer(1)

    def rb2Checked(self):
        self.pushButtonNext.setEnabled(True)
        self.answers[self.count].setAnswer(2)

    def rb3Checked(self):
        self.pushButtonNext.setEnabled(True)
        self.answers[self.count].setAnswer(3)

    def rb4Checked(self):
        self.pushButtonNext.setEnabled(True)
        self.answers[self.count].setAnswer(4)

    def pushButtonNextClicked(self):
        self.count += 1
        self.radioButtonsIsChecked()
        if self.answers[self.count].getAnswer() != 0:
            self.pushButtonNext.setEnabled(True)
        if self.count == len(self.answers):
            self.label.setText(self.resultTest())
            self.pushButtonNext.setEnabled(False)
            self.pushButtonPrev.setEnabled(False)
            self.radioButtonsActive(False)
        if self.count in range(1, len(self.answers)):
            self.pushButtonPrev.setEnabled(True)
        if self.count in range(0, len(self.answers)):
            self.radioButtonsReset()
            self.radioButtonsActive(True)
            self.label.setText(self.answers[self.count].getQuestion())
            self.pushButtonNext.setEnabled(False)
        self.label_2.setText(str(self.count))

    def radioButtonsReset(self):
        for rb in [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4]:
            rb.setAutoExclusive(False)
            rb.setChecked(False)
            rb.repaint()
            rb.setAutoExclusive(True)

    def radioButtonsActive(self, boolean_status):
        for rb in [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4]:
            if boolean_status:
                rb.setEnabled(True)
            else:
                rb.setEnabled(False)

    def radioButtonsIsChecked(self):
        if self.answers[self.count].getAnswer() == 1:
            self.radioButtonsReset()
            self.radioButton_1.setChecked(True)
            self.pushButtonNext.setEnabled(True)

        elif self.answers[self.count].getAnswer() == 2:
            self.radioButtonsReset()
            self.radioButton_2.setChecked(True)
            self.pushButtonNext.setEnabled(True)

        elif self.answers[self.count].getAnswer() == 3:
            self.radioButtonsReset()
            self.radioButton_3.setChecked(True)
            self.pushButtonNext.setEnabled(True)

        elif self.answers[self.count].getAnswer() == 4:
            self.radioButtonsReset()
            self.radioButton_4.setChecked(True)
            self.pushButtonNext.setEnabled(True)




    def pushButtonPrevClicked(self):
        self.count -= 1
        if self.count == 0:
            self.pushButtonPrev.setEnabled(False)
        self.label.setText(self.answers[self.count].getQuestion())
        self.pushButtonNext.setText("Next")
        self.radioButtonsIsChecked()
        self.label_2.setText(str(self.count))

    def resultTest(self):
        s = 0
        for i in range(len(self.answers)):
            s += self.answers[i].getAnswer()
        if s in range(25, 50):
            return statuses[0]
        elif s in range(50, 60):
            return statuses[1]
        elif s in range(60, 70):
            return statuses[2]
        elif s in range(70, 81):
            return statuses[3]
        else:
            return 'Вот не надо врать!!!'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Prog()
    form.show()
    app.exec()

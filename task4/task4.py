import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task4.ui', self)
        self.setFixedSize(650, 400)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.user)

    def start(self):
        self.pushButton.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.spinBox_2.setEnabled(True)
        self.listWidget.setEnabled(True)
        self.listWidget.clear()

    def take_a_rock(self, sender, num):
        prev = self.spinBox.value()
        if self.spinBox.value() - num <= 0:
            self.listWidget.addItem(f"{sender}: из {prev} взял {num} камней, в куче осталось: 0")
            self.listWidget.addItem(f"{sender} побеждает!")
            self.pushButton.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.spinBox_2.setEnabled(False)
            self.listWidget.setEnabled(False)
        else:
            self.spinBox.setValue(self.spinBox.value() - num)
            self.listWidget.addItem(f"{sender}: из {prev} взял {num} камней, в куче осталось: {self.spinBox.value()}")

    def user(self):
        print(self.spinBox_2.value())
        self.take_a_rock(str("Игрок"), self.spinBox_2.value())
        self.computer()

    def computer(self):
        if not self.spinBox.isEnabled():
            com_num = self.spinBox.value() % 4
            self.take_a_rock(str("Компьютер"), com_num)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task2.ui', self)
        self.setFixedSize(700, 325)

        self.addButton.clicked.connect(self.addRecord)

    def addRecord(self):
        text = self.lineEdit.text()
        date = self.calendarWidget.selectedDate().toPyDate()
        time = self.timeEdit.time().toPyTime()

        self.listWidget.addItem((f"{date} {time} {text}"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

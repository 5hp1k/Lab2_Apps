import difflib as df
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task5.ui', self)
        self.setFixedSize(811, 533)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.pushButton.clicked.connect(self.compare)

    def compare(self):
        str1 = self.textEdit.toPlainText()
        str2 = self.textEdit_2.toPlainText()

        y = df.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100
        if float(self.doubleSpinBox.text()) >= round(y, 2):
            self.statusBar.showMessage(f'Тексты совпадают на {round(y, 2)}%')
            self.statusBar.setStyleSheet('background-color: green')
        else:
            self.statusBar.showMessage(f'Тексты совпадают на {round(y, 2)}%')
            self.statusBar.setStyleSheet('background-color: red')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

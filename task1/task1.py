import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task1.ui', self)
        self.setFixedSize(400, 380)

        self.group1 = QButtonGroup(self)
        self.group2 = QButtonGroup(self)
        self.group3 = QButtonGroup(self)

        self.group1.addButton(self.redButton1)
        self.group1.addButton(self.whiteButton1)
        self.group1.addButton(self.blueButton1)

        self.group2.addButton(self.redButton2)
        self.group2.addButton(self.whiteButton2)
        self.group2.addButton(self.blueButton2)

        self.group3.addButton(self.redButton3)
        self.group3.addButton(self.whiteButton3)
        self.group3.addButton(self.blueButton3)

        self.flagButton.clicked.connect(self.updateLabels)

    def updateLabels(self):
        color1 = self.getSelectedColour(self.redButton1, self.whiteButton1, self.blueButton1)
        color2 = self.getSelectedColour(self.redButton2, self.whiteButton2, self.blueButton2)
        color3 = self.getSelectedColour(self.redButton3, self.whiteButton3, self.blueButton3)

        self.label1.setText(color1)
        self.label2.setText(color2)
        self.label3.setText(color3)

    def getSelectedColour(self, red, white, blue):
        if red.isChecked():
            return 'Красный'
        elif white.isChecked():
            return 'Белый'
        elif blue.isChecked():
            return 'Синий'
        else:
            return 'Без цвета'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

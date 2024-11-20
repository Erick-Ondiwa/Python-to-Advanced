import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt


class Clock(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        self.setLayout(hbox)


def main():
    application = QApplication(sys.argv)
    clock = Clock()

    clock.show()
    sys.exit(application.exec_())

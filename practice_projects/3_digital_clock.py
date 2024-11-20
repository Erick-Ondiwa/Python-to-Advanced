import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt


class Clock(QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QLabel("12:00:00", self)

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.time_label)

        self.setLayout(hbox)


def main():
    application = QApplication(sys.argv)
    clock = Clock()

    clock.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

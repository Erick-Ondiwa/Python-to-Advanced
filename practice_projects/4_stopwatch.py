import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QPushButton)
from PyQt5.QtCore import QTime, QTimer, Qt


class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)

        self.initUI()

    def initUI(self):
        # Create a central widget for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addWidget(hbox)

        central_widget.setLayout(vbox)


def main():
    application = QApplication(sys.argv)
    window = Clock()

    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QPushButton)
from PyQt5.QtCore import QTime, QTimer, Qt


class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00", self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)

        self.hours = QTime.hour()
        self.minutes = QTime.minute()
        self.seconds = QTime.second()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.initUI()

    def start(self):
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.time_label.setText("00:00:00")

    def update_time(self):
        self.hours = QTime.hour()
        self.minutes = QTime.minute()
        self.seconds = QTime.second()

    def initUI(self):
        # Create a central widget for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.time_label.setText(f"{self.hours}: {self.minutes}: {self.seconds}")

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        vbox.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.time_label)

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        central_widget.setLayout(vbox)


def main():
    application = QApplication(sys.argv)
    window = Clock()

    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

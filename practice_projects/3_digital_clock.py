import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt


class Clock(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.time_label = QLabel("12:00:00", self)

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.time_label)

        self.setLayout(hbox)

        # Connecting the timer function with the time function
        self.timer.timeout.connect(self.get_time)
        self.timer.start(1000)

        self.get_time()

    def get_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")

        self.time_label.setText(current_time)


def main():
    application = QApplication(sys.argv)
    clock = Clock()

    clock.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)

        self.init_gui()

    def init_gui(self):
        self.button = QPushButton("Save", self)  # Creates a button labeled SAVE
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("background-color: green;"
                             "font-size: 30px")

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Saved Successfully!")
        self.button.setText("Saved")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Save", self)  # Creates a button labeled SAVE
        self.setGeometry(0, 0, 500, 500)
        self.label = QLabel(" ", self)

        self.init_gui()

    def init_gui(self):
        self.button.setGeometry(150, 200, 100, 50)
        self.button.setStyleSheet("background-color: blue;"
                                  "font-size: 30px;"
                                  "border-radius:5px;"
                                  "cursor:pointer;")

        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("color:green;"
                                 "font-size:20px;"
                                 "font-family:Roboto;")

    def on_click(self):
        self.button.setText("Saved")
        self.label.setText("Saved Successfully!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)

        self.name_edit = QLineEdit(self)
        self.submit_button = QPushButton("SUBMIT", self)

        self.init_gui()

    def init_gui(self):
        self.name_edit.setGeometry(10, 10, 150, 20)
        self.name_edit.setPlaceholderText("Type your name here")
        self.submit_button.setGeometry(165, 10, 50, 20)

        # Connecting the submit button with the submit_details function
        self.submit_button.clicked.connect(self.submit_details)

    def submit_details(self):
        name = self.name_edit.text()

        print(f"Kind regards,\n{name}.")


def main():
    application = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()


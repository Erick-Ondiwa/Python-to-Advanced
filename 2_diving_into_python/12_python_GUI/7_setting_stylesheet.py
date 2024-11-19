import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_gui()

    def init_gui(self):
        pass


def main():
    application = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
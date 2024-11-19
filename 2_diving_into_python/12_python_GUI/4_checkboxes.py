import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QCheckBox
from PyQt5.QtCore import Qt  # The QtCore module contains non GUI classes relevant to PyQt5


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)

        self.male = QCheckBox("Male", self)
        self.label = QLabel(" ", self)

        self.init_gui()

    def init_gui(self):
        self.male.setGeometry(50, 50, 200, 50)

        self.male.setChecked(False)
        self.male.stateChanged.connect(self.checkbox)
        self.label.setGeometry(50, 80, 200, 50)
        # self.label.setText(" ")

    def checkbox(self, state):
        return "male" if state == Qt.Checked else "female"



def main():
    application = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()



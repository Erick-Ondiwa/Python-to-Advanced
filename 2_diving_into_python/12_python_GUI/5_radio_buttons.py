import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)

        self.visa = QRadioButton("Visa", self)
        self.mastercard = QRadioButton("Mastercard", self)
        self.giftcard = QRadioButton("Gift Card", self)

        self.online = QRadioButton("Online", self)
        self.in_store = QRadioButton("In Store", self)

        # Creating button groups
        self.button_group_1 = QButtonGroup(self)
        self.button_group_2 = QButtonGroup(self)

        self.init_gui()

    def init_gui(self):
        self.visa.setGeometry(0, 50, 200, 30)
        self.mastercard.setGeometry(0, 100, 200, 30)
        self.giftcard.setGeometry(0, 150, 200, 30)

        self.online.setGeometry(0, 200, 200, 30)
        self.in_store.setGeometry(0, 250, 200, 30)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 20px;"
                           "font-family: Roboto"
                           "padding: 10px"
                           "}")

        # Adding the buttons to the groups
        self.button_group_1.addButton(self.visa)
        self.button_group_1.addButton(self.mastercard)
        self.button_group_1.addButton(self.giftcard)

        self.button_group_2.addButton(self.online)
        self.button_group_2.addButton(self.in_store)

        # Connecting the buttons to the payment_mode function
        self.visa.toggled.connect(self.payment_mode)
        self.mastercard.toggled.connect(self.payment_mode)
        self.giftcard.toggled.connect(self.payment_mode)

        self.online.toggled.connect(self.payment_mode)
        self.in_store.toggled.connect(self.payment_mode)

    def payment_mode(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            print(f"{radio_button.text()} is checked")



def main():
    application = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

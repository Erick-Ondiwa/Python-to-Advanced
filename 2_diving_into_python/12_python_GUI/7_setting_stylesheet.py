import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.previous_button = QPushButton("Previous")
        self.save_button = QPushButton("SAVE")
        self.next_button = QPushButton("Next")

        self.init_gui()

    def init_gui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.previous_button)
        hbox.addWidget(self.save_button)
        hbox.addWidget(self.next_button)

        central_widget.setLayout(hbox)

        # Setting object name to each button to enable selection
        self.previous_button.setObjectName("previous_button")
        self.save_button.setObjectName("save_button")
        self.next_button.setObjectName("next_button")

        self.setStyleSheet("""
            QPushButton{
                font-size: 15px;
                font-family: Roboto;
                padding:10px 30px;
                border: 3px solid green;
                border-radius: 5px;
            }
            
            QPushButton#previous_button{
                background-color:red;
            }
            
            QPushButton#save_button{
                background-color:green;
            }
            
            QPushButton#next_button{
                background-color:yellow;
            }
            
            QPushButton#save_button:hover{
                background-color:blue;
            }
        """)


def main():
    application = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    # application.exec_() # Not ideal for production-level code, as it might leave the program in
    #                        an undefined state after the event loop ends
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
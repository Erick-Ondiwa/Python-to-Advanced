import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt  # This class is used for alignments


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(700, 300, 200, 200)
        self.setWindowIcon(QIcon(" "))  # Add a relevant file path to your Image Icon

        # Adding Labels
        label1 = QLabel("Erick Ondiwa", self)
        label1.setGeometry(0, 0, 200, 50)
        label1.setFont(QFont("Roboto", 30))
        label1.setStyleSheet("color: blue;"
                             "background-color: #6fdcf7;"
                             "text-decoration: underline;")  # You can use RGB or HEX values

        # Setting Alignments
        # label1.setAlignment(Qt.AlignTop)  # Vertically aligns text to the top
        # label1.setAlignment(Qt.AlignBottom)  # Vertically aligns text to the bottom
        # label1.setAlignment(Qt.AlignVCenter)  # Vertically aligns text to the center
        #
        # label1.setAlignment(Qt.AlignRight)  # horizontally aligns text to the right
        # label1.setAlignment(Qt.AlignHCenter)  # horizontally aligns text to the center
        # label1.setAlignment(Qt.AlignLeft)  # horizontally aligns text to the left

        # label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # horizontally aligns text to the
        # # center
        # label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # horizontally and vertically
        # aligns text to the center
        label1.setAlignment(Qt.AlignCenter)  # horizontally and vertically aligns text to the center

        # Adding an Image to a GUI
        image_label = QLabel(self) # Creating an empty label
        image_label.setGeometry(0, 0, 250, 250)

        img = QPixmap("file_path")
        image_label.setPixmap(img)  # Adding the image to the label

        image_label.setScaledContents(True)  # This enables the image to fit into the label size


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    # app.exec_() # Not ideal for production-level code, as it might leave the program in an
    #                 undefined state after the event loop ends.
    sys.exit(app.exec_())  # Passes exit code to the OS for clean termination.


if __name__ == "__main__":
    main()

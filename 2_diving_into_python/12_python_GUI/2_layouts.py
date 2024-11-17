import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create labels
        labels = [
            QLabel("#1"),
            QLabel("#2"),
            QLabel("#3"),
            QLabel("#4"),
            QLabel("#5"),
        ]

        # Set styles for labels
        colors = ["red", "blue", "green", "yellow", "grey"]
        for label, color in zip(labels, colors):
            label.setStyleSheet(f"background-color: {color};")

        # Add labels to a vertical layout
        # grid = QGridLayout()  # QHBoxLayout(), QGridLayout
        # for label in labels:
        #     grid.addWidget(label)

        # For grid Layout
        # Create a grid layout and add labels
        grid = QGridLayout()
        grid.addWidget(labels[0], 0, 0)  # Row 0, Column 0
        grid.addWidget(labels[1], 0, 1)  # Row 0, Column 1
        grid.addWidget(labels[2], 1, 0)  # Row 1, Column 0
        grid.addWidget(labels[3], 1, 1)  # Row 1, Column 1
        grid.addWidget(labels[4], 2, 0, 1, 2)  # Row 2, Columns 0-1 (span 2 columns)

        # Set layout for the central widget
        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

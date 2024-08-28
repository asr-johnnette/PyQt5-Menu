import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGroupBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        button = QPushButton("Click me")

        # Create layout
        layout = QVBoxLayout()

        # Create a group box
        group_box = QGroupBox("My Group")
        group_box_layout = QVBoxLayout()
        group_box_layout.addWidget(label1)
        group_box_layout.addWidget(label2)
        group_box.setLayout(group_box_layout)

        # Add widgets and group box to the main layout
        layout.addWidget(group_box)
        layout.addWidget(button)

        # Set layout for the window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Create layout
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        # Group widgets
        group1 = QGroupBox("Group 1")
        group1.setLayout(hbox1)
        hbox1.addWidget(label1)
        hbox1.addWidget(button1)

        group2 = QGroupBox("Group 2")
        group2.setLayout(hbox2)
        hbox2.addWidget(label2)
        hbox2.addWidget(button2)

        vbox.addWidget(group1)
        vbox.addWidget(group2)

        # Set layout for the window
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
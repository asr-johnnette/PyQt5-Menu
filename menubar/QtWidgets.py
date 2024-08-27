import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle('Simple QWidget Example')
        self.setGeometry(300, 300, 200, 200)

        # Create widgets
        self.label = QLabel('Enter your name:')
        self.name_input = QLineEdit()
        self.name_input.setMinimumWidth(100)
        self.name_input.setMaximumWidth(300)
        self.greet_button = QPushButton('Greet')
        self.greet_button.setFixedWidth(100)
        self.greeting_label = QLabel('')

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.greet_button)
        layout.addWidget(self.greeting_label)

        # Set the layout for the main window
        self.setLayout(layout)

        # Connect the button click to a function
        self.greet_button.clicked.connect(self.greet)

    def greet(self):
        name = self.name_input.text()
        if name:
            self.greeting_label.setText(f"Hello, {name}!")
        else:
            self.greeting_label.setText("Please enter a name.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())
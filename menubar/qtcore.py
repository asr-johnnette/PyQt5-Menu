import sys
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal, QTimer

class MyObject(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timeout)

    def start(self):
        self.timer.start(1000)

    def on_timeout(self):
        print("Timer elapsed!")
        self.finished.emit()

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    obj = MyObject()
    obj.start()

    obj.finished.connect(lambda: print("Finished!"))
    app.exec_()
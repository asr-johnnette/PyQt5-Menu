from PyQt5.QtWidgets import QMainWindow, QMenu, QApplication, QAction
import sys

class MainMenuBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Example")
        self.setGeometry(300, 300, 600, 400)
        self.createMenuBar()

    def createMenuBar(self):
        
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)

        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        
        # Creating menus using a title

        # Add actions (New, Open, Save, Exit) to "File" menu
        newAction = QAction("New", self)
        openAction = QAction("Open", self)
        saveAction = QAction("Save", self)
        exitAction = QAction("Exit", self)

        # Add actions to the File menu
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addSeparator()  # Add a separator line between Save and Exit
        fileMenu.addAction(exitAction)

        # Add "Edit" menu (empty for now)
        editMenu = menuBar.addMenu("Edit")

        # Add "View" menu (empty for now)
        viewMenu = menuBar.addMenu("View")

        # Add "Help" menu (empty for now)
        helpMenu = menuBar.addMenu("Help")

        # Optional: Connect actions to a function
        exitAction.triggered.connect(self.close)  # Close the application when Exit is clicked


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenuBar()
    window.show()
    sys.exit(app.exec_())
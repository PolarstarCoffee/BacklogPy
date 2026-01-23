from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton
import sys
import backlogObj
import backlogEdit


# Entry point for the application
# This is a simple PyQt6 window that can be expanded later

class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #main group for adding other widgets later
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Backlog App")
        self.setGeometry(100, 100, 300, 200)
        
        button = QPushButton("Exit")
        button.pressed.connect(self.close)
        self.show()
app = QApplication(sys.argv)
window = EntryWindow()
app.exec()
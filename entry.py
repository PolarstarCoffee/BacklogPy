from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton
import sys
import backlogObj
import backlogEdit
import threadWorker


# Entry point for the application
# This is a simple PyQt6 window that can be expanded later

class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backlog App: NAME WIP")
        #set up the central widget for the main window
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        
        
        self.setGeometry(200, 200, 600, 400)
        self.show()
#core window loop for the application





app = QApplication(sys.argv)
window = EntryWindow()
app.exec()
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys
import backlogObj


# Entry point for the application
# This is a simple PyQt6 window that can be expanded later

class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backlog App")
        self.setGeometry(100, 100, 300, 200)
        
        button = QPushButton("Exit")
        button.pressed.connect(self.close)
        self.setCentralWidget(button)
        self.show()
app = QApplication(sys.argv)
window = EntryWindow()
app.exec()
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QtGui
import sys
import backlogObj


class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backlog App")
        self.setGeometry(100, 100, 300, 200)
        
        button = QPushButton("Exit")
        button.pressed.connect(self.close)
        self.setCentralWidget(button)
        self.show()
app = QApplication([])
window = EntryWindow()
app.exec()
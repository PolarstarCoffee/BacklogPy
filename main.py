import sys
import time
import models.backlogObj
import managers.backlogManager as backlogManager
import managers.threadWorker as threadWorker
from PyQt6.QtCore import QThreadPool
from PyQt6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QApplication, QMainWindow, QLabel, QPushButton

class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backlog App: NAME WIP")
        self.threadpool = QThreadPool()
        centralWidget = QWidget()
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EntryWindow()
    win.show()
    sys.exit(app.exec())
    
    
    
    
    
# self.button = QPushButton("Start long task")
# self.button.clicked.connect(self.start_long_task)
    
    
         
        # def execute_this_fn(self):
        #     for n in range(0,5):
        #         print(f"Working...{n+1}")
        #         time.sleep(1)
        #     return "Done."
        
        # def print_output(self, s):
        #     print(s)
        # def thread_complete(self):
        #     print("Thread complete.")
        # def start_long_task(self):
        #     # Pass the function to execute in the thread
        #     worker = threadWorker.threadWorker(self.execute_this_fn)
        #     worker.signals.result.connect(self.print_output)
        #     worker.signals.finished.connect(self.thread_complete)
        #     self.threadpool.start(worker)        
    
    
    #Next steps:
    #1.add entry dialog 
        #validation for title, description, status, thumbnail, image paths
    #2. display entries in a list view, with the ability to select an entry
    #3. edit the selected entry in a dialog, with validation 
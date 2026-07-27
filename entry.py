import sys
import time
import backlogObj
import backlogEdit
import threadWorker
from PyQt6.QtCore import QThreadPool
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QApplication, QMainWindow, QLabel, QPushButton

# Entry point for the application
# This is a simple PyQt6 window that can be expanded later

class EntryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backlog App: NAME WIP")
        self.threadpool = QThreadPool()
        self.button = QPushButton("Start long task")
        self.button.clicked.connect(self.start_long_task)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
    def execute_this_fn(self):
        for n in range(0,5):
            print(f"Working...{n+1}")
            time.sleep(1)
        return "Done."
    
    def print_output(self, s):
        print(s)
    def thread_complete(self):
        print("Thread complete.")
    def start_long_task(self):
        # Pass the function to execute in the thread
        worker = threadWorker.threadWorker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        self.threadpool.start(worker)        
#core window loop for the application




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EntryWindow()
    win.show()
    sys.exit(app.exec())
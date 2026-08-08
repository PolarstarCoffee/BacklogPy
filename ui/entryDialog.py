from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLineEdit,
    QVBoxLayout,
    QPushButton
)
import sys
import models.backlogObj as backlogObj

class EntryDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Backlog Entry")

        layout = QVBoxLayout()

        self.titleInput = QLineEdit()
        self.titleInput.setPlaceholderText("Enter title...")

        self.saveButton = QPushButton("Save")

        layout.addWidget(self.titleInput)
        layout.addWidget(self.saveButton)

        self.setLayout(layout)
        
        self.saveButton.clicked.connect(self.save_entry)
    def save_entry(self):
        title = self.titleInput.text()
        entry = backlogObj.backlogObj(title=title)
        self.accept()  # Close the dialog and return QDialog.Accepted
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EntryDialog()
    win.show()
    sys.exit(app.exec())
    
    
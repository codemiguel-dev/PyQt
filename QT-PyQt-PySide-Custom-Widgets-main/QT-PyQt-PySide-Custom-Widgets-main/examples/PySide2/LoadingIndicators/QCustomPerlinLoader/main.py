import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide2.QtGui import QColor
from Custom_Widgets.QCustomLoadingIndicators import QCustomPerlinLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create a loader widget with the main window as parent
        self.loader = QCustomPerlinLoader()

        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)

        self.layout.addWidget(self.loader)
        self.layout.setAlignment(self.loader, Qt.AlignCenter)  # Align loader widget to the center of the layout

        self.setCentralWidget(self.centralwidget)
        self.resize(800, 450)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create an instance of MainWindow
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec())


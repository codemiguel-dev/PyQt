from PyQt5.QtWidgets import QSplashScreen, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys

class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showMessage("Cargando...", Qt.AlignBottom | Qt.AlignCenter, Qt.white)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplicación Principal')
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        label = QLabel('Bienvenido a la Aplicación Principal')
        layout.addWidget(label)
        
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Crear y mostrar el splash screen
    pixmap = QPixmap("image/google.png")  # Ruta a tu imagen de splash
    splash = SplashScreen(pixmap)
    splash.show()
    
    # Crear la ventana principal
    main_window = MainWindow()
    
    # Mostrar la ventana principal después de un retraso
    QTimer.singleShot(3000, splash.close)  # El splash screen se mostrará durante 3 segundos
    QTimer.singleShot(3000, main_window.show)  # Mostrar la ventana principal después de 3 segundos
    
    sys.exit(app.exec_())

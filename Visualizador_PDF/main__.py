import sys
import os
import fitz  # PyMuPDF
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QScrollArea
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class PDFViewer(QMainWindow):
    def __init__(self, pdf_path):
        super().__init__()
        self.setWindowTitle('PDF Viewer')
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crear un diseño vertical
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Crear un área de desplazamiento
        self.scroll_area = QScrollArea()
        layout.addWidget(self.scroll_area)

        # Crear un widget para contener las imágenes
        self.image_widget = QWidget()
        self.scroll_area.setWidget(self.image_widget)
        self.scroll_area.setWidgetResizable(True)

        # Crear un diseño vertical para el widget de imágenes
        self.image_layout = QVBoxLayout()
        self.image_widget.setLayout(self.image_layout)

        # Cargar el archivo PDF
        self.load_pdf(pdf_path)

    def load_pdf(self, pdf_path):
        # Abrir el archivo PDF
        pdf_document = fitz.open(pdf_path)

        # Mostrar las páginas como imágenes
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            label = QLabel()
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            self.image_layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Obtener el directorio del script actual
    current_dir = os.path.dirname(__file__)

    # Construir la ruta al archivo PDF relativa al directorio actual
    pdf_path = os.path.join(current_dir, "pdf/venta_20240807_203120.pdf")

    # Verificar la existencia del archivo
    if not os.path.exists(pdf_path):
        print(f"El archivo no se encuentra: {pdf_path}")
        sys.exit(1)

    viewer = PDFViewer(pdf_path)
    viewer.show()
    sys.exit(app.exec_())

import sys
import os
import fitz  # PyMuPDF
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFileDialog, QScrollArea
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class PDFViewer(QMainWindow):
    def __init__(self):
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

        # Crear un botón para abrir el diálogo de archivos
        self.button = QPushButton('Select PDF File')
        self.button.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.button)

    def open_file_dialog(self):
        # Abrir un diálogo para seleccionar un archivo PDF
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("PDF Files (*.pdf)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                self.load_pdf(file_paths[0])

    def load_pdf(self, pdf_path):
        # Limpiar las imágenes existentes
        for i in reversed(range(self.image_layout.count())):
            widget = self.image_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

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
    viewer = PDFViewer()
    viewer.show()
    sys.exit(app.exec_())

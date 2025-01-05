from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class DragDropExample(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.list_widget1 = QListWidget()
        self.list_widget2 = QListWidget()

        # Habilitar arrastrar en el primer QListWidget
        self.list_widget1.setDragEnabled(True)

        # Habilitar que el segundo QListWidget acepte soltar
        self.list_widget2.setAcceptDrops(True)
        self.list_widget2.setDragDropMode(QListWidget.DropOnly)

        # Añadir algunos elementos a la primera lista
        for i in range(5):
            item = QListWidgetItem(f"Card {i+1}")
            self.list_widget1.addItem(item)

        layout.addWidget(self.list_widget1)
        layout.addWidget(self.list_widget2)

        self.setLayout(layout)
        self.setWindowTitle('Drag and Drop Example')

if __name__ == "__main__":
    app = QApplication([])
    window = DragDropExample()
    window.show()
    app.exec_()

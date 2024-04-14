import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QStatusBar, QAction, QMessageBox, QVBoxLayout, QMenu
from PyQt5.QtGui import QIcon


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menú Desplegable con Botones')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Crear el menú desplegable
        self.menu_desplegable = QMenu(self)
        opciones = ['Habitacion propia', 'habitacion huesped', 'sala', 'cocina']
        for opcion_texto in opciones:
            accion = QAction(opcion_texto, self)
            accion.triggered.connect(self.mostrar_botones)
            accion.setData(opcion_texto)  # Almacenar el nombre de la opción en los datos de la acción
            self.menu_desplegable.addAction(accion)

        # Agregar el menú desplegable a la barra de menú
        self.menuBar().addMenu(self.menu_desplegable)

        self.layout.addWidget(self.menu_desplegable)

    def mostrar_botones(self):
        opcion = self.sender().data()  # Obtener el nombre de la opción seleccionada
        # Limpiar el diseño antes de agregar nuevos botones
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Crear 2 botones en función de la opción seleccionada
        for i in range(1, 2):
            boton_texto = f'foco {i} de {opcion}'
            boton = QPushButton(boton_texto)
            self.layout.addWidget(boton)
            
        for i in range(2, 3):
            boton_texto = f'puerta {i} de {opcion}'
            boton = QPushButton(boton_texto)
            self.layout.addWidget(boton)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
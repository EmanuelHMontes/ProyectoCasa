import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QMessageBox, QPushButton, QLabel, QVBoxLayout, QWidget, QSlider, QHBoxLayout


class ControlDeIluminacion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Control de Luces')
        self.setGeometry(100, 100, 400, 300)

        # Crear menú para seleccionar la habitación
        self.menu_habitaciones = QMenu('Habitaciones', self)

        # Habitación 1
        self.habitacion1_menu = self.menu_habitaciones.addMenu('Habitación 1')
        self.create_actions(self.habitacion1_menu)

        # Habitación 2
        self.habitacion2_menu = self.menu_habitaciones.addMenu('Habitación 2')
        self.create_actions(self.habitacion2_menu)

        # Crear menú principal
        self.menu_principal = self.menuBar()
        self.menu_principal.addMenu(self.menu_habitaciones)

        # Crear botones para encender y apagar la luz
        self.btn_encender = QPushButton('Encender', self)
        self.btn_encender.clicked.connect(self.encender_luz)

        self.btn_apagar = QPushButton('Apagar', self)
        self.btn_apagar.clicked.connect(self.apagar_luz)

        # Crear barra deslizante para seleccionar el nivel de iluminación
        self.slider_iluminacion = QSlider()
        self.slider_iluminacion.setOrientation(1)
        self.slider_iluminacion.setMinimum(0)
        self.slider_iluminacion.setMaximum(100)
        self.slider_iluminacion.setValue(50)
        self.slider_iluminacion.setTickInterval(10)
        self.slider_iluminacion.setTickPosition(2)

        # Crear etiqueta para mostrar el nivel de iluminación
        self.lbl_iluminacion = QLabel('Nivel de Iluminación: 50', self)

        # Conectar el cambio en la barra deslizante a la función de actualización
        self.slider_iluminacion.valueChanged.connect(self.actualizar_iluminacion)

        # Crear layout vertical para los botones y la barra deslizante
        layout = QVBoxLayout()
        layout.addWidget(self.btn_encender)
        layout.addWidget(self.btn_apagar)
        layout.addWidget(self.lbl_iluminacion)
        layout.addWidget(self.slider_iluminacion)

        # Crear widget contenedor para el layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()
        

    def create_actions(self, menu):
        # Acciones para encender y apagar luces
        self.action_encender = QAction('Encender Foco', menu)
        self.action_encender.triggered.connect(lambda: self.encender_luz(menu.title()))

        self.action_apagar = QAction('Apagar Foco', menu)
        self.action_apagar.triggered.connect(lambda: self.apagar_luz(menu.title()))

        # Agregar las acciones al menú de la habitación
        menu.addAction(self.action_encender)
        menu.addAction(self.action_apagar)

    def encender_luz(self, habitacion):
        QMessageBox.information(self, 'Luz Encendida', f'Luz encendida en la habitación {habitacion}')

    def apagar_luz(self, habitacion):
        QMessageBox.information(self, 'Luz Apagada', f'Luz apagada en la habitación {habitacion}')

    def actualizar_iluminacion(self):
        nivel_iluminacion = self.slider_iluminacion.value()
        self.lbl_iluminacion.setText(f'Nivel de Iluminación: {nivel_iluminacion}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ControlDeIluminacion()
    sys.exit(app.exec_())

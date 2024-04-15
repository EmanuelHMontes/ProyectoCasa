import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QMessageBox, QPushButton, QLabel, QVBoxLayout, QWidget, QSlider, QHBoxLayout
from PyQt5.QtGui import QIcon
from pathlib import Path

def absPath(nombre):
    return str( Path(__file__).parent.absolute() / nombre)


class ControlDeIluminacion(QMainWindow):
    def __init__(self, habitacion):
        super().__init__()

        self.initUI(habitacion)

    def initUI(self, habitacion):
        self.setWindowTitle('Control de Luces')
        self.setGeometry(100, 100, 400, 300)

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

        self.habitacion = habitacion

        self.show()

    def encender_luz(self):
        QMessageBox.information(self, 'Luz Encendida', f'Luz encendida en la habitación {self.habitacion}')

    def apagar_luz(self):
        QMessageBox.information(self, 'Luz Apagada', f'Luz apagada en la habitación {self.habitacion}')

    def actualizar_iluminacion(self):
        nivel_iluminacion = self.slider_iluminacion.value()
        self.lbl_iluminacion.setText(f'Nivel de Iluminación: {nivel_iluminacion}')


class VentanaOpciones(QWidget):
    def __init__(self, habitacion):
        super().__init__()
        self.setWindowTitle(f"Casa Inteligente - {habitacion}")
        self.setGeometry(200, 200, 400, 300)
        
        #Agregar Icono
        Icono = QIcon(absPath("casa.png"))
        self.setWindowIcon(Icono)

        #Color de Venta Secundaria 
        self.setStyleSheet("background-color: #008B8B; color: black;")

        self.habitacion = habitacion
       
        self.estado_puerta = "cerrada"  # Estado inicial de la puerta
        self.estado_camara = "apagada"  # Estado inicial de la cámara

        layout = QVBoxLayout()

        # Título de la habitación
        label_habitacion = QLabel(f"{habitacion}", self)
        label_habitacion.setStyleSheet("font: bold 16pt; margin-bottom: 20px;")
        layout.addWidget(label_habitacion)

        # Botones de opciones
        
        self.boton_puerta = QPushButton(f"Puerta {self.estado_puerta}")
        self.boton_camara = QPushButton(f"Cámara {self.estado_camara}")

        # Conectar botones a las funciones correspondientes
        
        self.boton_puerta.clicked.connect(self.cambiar_estado_puerta)
        self.boton_camara.clicked.connect(self.cambiar_estado_camara)

        # Botón de regreso
        boton_regreso = QPushButton("← Regresar")
        boton_regreso.clicked.connect(self.regresar_a_ventana_principal)

        # Agregar widgets al layout
        
        layout.addWidget(self.boton_puerta)
        layout.addWidget(self.boton_camara)
        layout.addWidget(boton_regreso)

        # Agregar el control de iluminación
        self.control_iluminacion = ControlDeIluminacion(habitacion)
        layout.addWidget(self.control_iluminacion)

        self.setLayout(layout)

   

    def cambiar_estado_puerta(self):
        if self.estado_puerta == "cerrada":
            self.estado_puerta = "abierta"
        else:
            self.estado_puerta = "cerrada"
        self.boton_puerta.setText(f"Puerta {self.estado_puerta}")

    def cambiar_estado_camara(self):
        if self.estado_camara == "apagada":
            self.estado_camara = "encendida"
        else:
            self.estado_camara = "apagada"
        self.boton_camara.setText(f"Cámara {self.estado_camara}")

    def regresar_a_ventana_principal(self):
        self.close()  # Cerrar la segunda ventana
        ventana_principal.show()  # Mostrar de nuevo la ventana principal


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Casa Inteligente - Ventana Principal")
        self.setGeometry(100, 100, 400, 300)

        #CAMBIAR EL COLOR DE LA VENTANA PRINCIPAL
        self.setStyleSheet("background-color: #008B8B; color: black;")

        #Agregar Icono
        Icono = QIcon(absPath("casa.png"))
        self.setWindowIcon(Icono)

        layout = QVBoxLayout()

        # Botones principales
        boton_sala = QPushButton("Sala")
        boton_principal = QPushButton("Habitación Principal")
        boton_huesped = QPushButton("Habitación de Huésped")
        boton_comedor = QPushButton("Comedor")

        # Conectar botones a la función para abrir la segunda ventana
        boton_sala.clicked.connect(lambda: self.abrir_segunda_ventana("Sala"))
        boton_principal.clicked.connect(lambda: self.abrir_segunda_ventana("Habitación Principal"))
        boton_huesped.clicked.connect(lambda: self.abrir_segunda_ventana("Habitación de Huésped"))
        boton_comedor.clicked.connect(lambda: self.abrir_segunda_ventana("Comedor"))

        # Agregar botones al layout principal
        layout.addWidget(boton_sala)
        layout.addWidget(boton_principal)
        layout.addWidget(boton_huesped)
        layout.addWidget(boton_comedor)

        self.setLayout(layout)

    def abrir_segunda_ventana(self, habitacion):
        self.segunda_ventana = VentanaOpciones(habitacion)
        self.segunda_ventana.show()
        self.hide()  # Ocultar la ventana principal al abrir la segunda ventana
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())

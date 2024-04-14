import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Casa Inteligente - Ventana Principal")
        self.setGeometry(100, 100, 400, 300)

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

class VentanaOpciones(QWidget):
    def __init__(self, habitacion):
        super().__init__()
        self.setWindowTitle(f"Casa Inteligente - {habitacion}")
        self.setGeometry(200, 200, 400, 300)

        self.habitacion = habitacion
        self.estado_foco = "apagado"  # Estado inicial del foco
        self.estado_puerta = "cerrada"  # Estado inicial de la puerta
        self.estado_camara = "apagada"  # Estado inicial de la cámara

        layout = QVBoxLayout()

        # Título de la habitación
        label_habitacion = QLabel(f"{habitacion}", self)
        label_habitacion.setStyleSheet("font: bold 16pt; margin-bottom: 20px;")
        layout.addWidget(label_habitacion)

        # Botones de opciones
        self.boton_foco = QPushButton(f"Foco {self.estado_foco}")
        self.boton_puerta = QPushButton(f"Puerta {self.estado_puerta}")
        self.boton_camara = QPushButton(f"Cámara {self.estado_camara}")

        # Conectar botones a las funciones correspondientes
        self.boton_foco.clicked.connect(self.cambiar_estado_foco)
        self.boton_puerta.clicked.connect(self.cambiar_estado_puerta)
        self.boton_camara.clicked.connect(self.cambiar_estado_camara)

        # Botón de regreso
        boton_regreso = QPushButton("← Regresar")
        boton_regreso.clicked.connect(self.regresar_a_ventana_principal)

        # Agregar widgets al layout
        layout.addWidget(self.boton_foco)
        layout.addWidget(self.boton_puerta)
        layout.addWidget(self.boton_camara)
        layout.addWidget(boton_regreso)

        self.setLayout(layout)

    def cambiar_estado_foco(self):
        if self.estado_foco == "apagado":
            self.estado_foco = "encendido"
        else:
            self.estado_foco = "apagado"
        self.boton_foco.setText(f"Foco {self.estado_foco}")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())

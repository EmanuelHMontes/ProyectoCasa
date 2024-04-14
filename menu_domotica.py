from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ventana_opciones import VentanaOpciones

class CasaDomoticaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Casa Domótica - Menú Principal")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Botones principales del menú
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

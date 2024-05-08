from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QComboBox, QMessageBox, QPushButton, QHBoxLayout, QLineEdit, QTextEdit
from PyQt6.QtCore import QSize, Qt, QTimer
import sys, time, os
import control_motor


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()     

        #----------------------Config ventana------------------------#
        self.setFixedSize(QSize(500, 400))
        self.setWindowTitle("Motor a pasos")

        #----------------------elementos------------------------#
        self.girar90_boton = QPushButton("Girar 90 grados")
        self.girar90_boton.setFixedWidth(100)
        self.girar90_boton.setStyleSheet("font-size: 10px;")
        self.girar90_boton.setContentsMargins(0, 0, 0, 0)
        self.girar90_boton.clicked.connect(self.girar_90)

        self.girar180_boton = QPushButton("Girar 180 grados")
        self.girar180_boton.setFixedWidth(100)
        self.girar180_boton.setStyleSheet("font-size: 10px;")
        self.girar180_boton.setContentsMargins(0, 0, 0, 0)
        self.girar180_boton.clicked.connect(self.girar_180)

        self.girar270_boton = QPushButton("Girar 270 grados")
        self.girar270_boton.setFixedWidth(100)
        self.girar270_boton.setStyleSheet("font-size: 10px;")
        self.girar270_boton.setContentsMargins(0, 0, 0, 0)
        self.girar270_boton.clicked.connect(self.girar_270)

        self.posicion0_boton = QPushButton("Regresar a posicion inicial")
        self.posicion0_boton.setFixedWidth(140)
        self.posicion0_boton.setStyleSheet("font-size: 10px;")
        self.posicion0_boton.setContentsMargins(0, 0, 0, 0)
        self.posicion0_boton.clicked.connect(self.regresar)


        contenedor_uno = QVBoxLayout()
        contenedor_uno_cero = QHBoxLayout() #crea un layout que dispone los elementos en horizontal
        contenedor_uno_cero.setContentsMargins(10, 0, 0, 0) #se establecen espacios entre los componentes

        contenedor_uno.addLayout(contenedor_uno_cero)#toma el layout vertical como el layout principal de la ventana
        contenedor_uno_cero.addWidget(self.girar90_boton)
        contenedor_uno_cero.addWidget(self.girar180_boton)
        contenedor_uno_cero.addWidget(self.girar270_boton)
        contenedor_uno_cero.addWidget(self.posicion0_boton)




        widget = QWidget()
        widget.setLayout(contenedor_uno)
        self.setCentralWidget(widget)

    def girar_90(self):
        control_motor.moverAngulo(90, 0.001)
        print("mover")
    
    def girar_180(self):
        control_motor.moverAngulo(180, 0.001)
        print("mover")
    
    def girar_270(self):
        control_motor.moverAngulo(270, 0.001)
        print("mover")
    
    def regresar(self):
        control_motor.moverAngulo(0, 0.001)
        print("mover")

app = QApplication(sys.argv)
window = VentanaPrincipal()
window.show()
app.exec()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class VentanaInicioSesion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Iniciar Sesión")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Etiqueta y campo de texto para el nombre de usuario
        self.label_usuario = QLabel("Usuario:")
        self.input_usuario = QLineEdit()
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)

        # Etiqueta y campo de texto para la contraseña
        self.label_password = QLabel("Contraseña:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)  # Ocultar texto de la contraseña
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        # Botón para iniciar sesión
        boton_iniciar_sesion = QPushButton("Iniciar Sesión")
        boton_iniciar_sesion.clicked.connect(self.iniciar_sesion)
        layout.addWidget(boton_iniciar_sesion)

        # Botón para crear un nuevo usuario
        boton_crear_usuario = QPushButton("Crear Usuario")
        boton_crear_usuario.clicked.connect(self.crear_usuario)
        layout.addWidget(boton_crear_usuario)

        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.input_usuario.text().strip()
        contrasena = self.input_password.text().strip()

        # Aquí puedes agregar tu lógica de autenticación
        if usuario == "admin" and contrasena == "admin123":
            QMessageBox.information(self, "Inicio de Sesión", "¡Inicio de sesión exitoso!")
        else:
            QMessageBox.warning(self, "Inicio de Sesión", "Usuario o contraseña incorrectos.")

    def crear_usuario(self):
        QMessageBox.information(self, "Crear Usuario", "Función para crear usuario aún no implementada.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_inicio = VentanaInicioSesion()
    ventana_inicio.show()
    sys.exit(app.exec_())

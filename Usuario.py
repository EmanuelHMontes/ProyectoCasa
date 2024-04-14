import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

class CrearUsuarioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Nuevo Usuario")
        self.setGeometry(100, 100, 400, 200)

        # Cambiar el color de fondo y el color del texto con hojas de estilo
        self.setStyleSheet("background-color: black; color: white;")

        self.label_nombre = QLabel(self)
        self.label_nombre.setText("Nombre de Usuario:")
        self.label_nombre.move(50, 30)

        self.label_nombre.setStyleSheet("font: bold;")  # Estilo para la etiqueta de nombre de usuario

        self.entry_nombre = QLineEdit(self)
        self.entry_nombre.move(200, 30)

        self.label_contrasena = QLabel(self)
        self.label_contrasena.setText("Contraseña:")
        self.label_contrasena.move(50, 70)

        self.label_contrasena.setStyleSheet("font: bold;")  # Estilo para la etiqueta de contraseña

        self.entry_contrasena = QLineEdit(self)
        self.entry_contrasena.setEchoMode(QLineEdit.Password)
        self.entry_contrasena.move(200, 70)

        self.boton_crear = QPushButton('Crear Usuario', self)
        self.boton_crear.move(150, 120)
        self.boton_crear.clicked.connect(self.crear_usuario)

        # Estilo para el botón
        self.boton_crear.setStyleSheet("background-color: white; color: black;")

    def crear_usuario(self):
        nombre = self.entry_nombre.text()
        contrasena = self.entry_contrasena.text()

        if nombre == '' or contrasena == '':
            QMessageBox.critical(self, "Error", "Por favor ingresa un nombre y una contraseña.")
            return

        if nombre in usuarios:
            QMessageBox.critical(self, "Error", f"El usuario '{nombre}' ya existe. Por favor elige otro nombre.")
            return

        # Guardar el usuario y contraseña en el diccionario
        usuarios[nombre] = contrasena
        QMessageBox.information(self, "Éxito", "Usuario creado exitosamente.")

        # Limpiar las entradas después de crear un usuario
        self.entry_nombre.clear()
        self.entry_contrasena.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CrearUsuarioApp()
    ventana.show()
    sys.exit(app.exec_())

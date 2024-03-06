
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class ButtonExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):  # crea un objeto de diseño vertical
        layout = QVBoxLayout()

        # Crear 2 botones a usar
        self.btn1 = QPushButton('Foco Sala Apagado')
        self.btn2 = QPushButton('Foco Cuarto Apagado')

        # Conectar botones a funciones
        self.btn1.clicked.connect(lambda: self.toggle_foco(self.btn1)) #lambda como señar anonima
        self.btn2.clicked.connect(lambda: self.toggle_foco(self.btn2)) #espera una función que será ejecutado cuando se haga clic en el botón

        # Agregar botones al diseño
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

        # Configurar la ventana principal
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Control de Focos')

        # Mostrar la ventana
        self.show()

    def toggle_foco(self, button):  #un metodo de clase que alterna entre foco apagado y foco prendido
        if button.text() == 'Foco Sala Apagado':
            button.setText('Foco Cuarto Encendido')
            print('1')  # Representa foco encendido
        else:
            button.setText('Foco Sala Apagado')
            print('0')  # Representa foco apagado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonExample()
    sys.exit(app.exec_())
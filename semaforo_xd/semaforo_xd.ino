// Definición de pines para el primer semáforo
const int rojo1Pin = 5;
const int amarillo1Pin = 18;
const int verde1Pin = 2;
const int boton1Pin = 32;

// Definición de pines para el segundo semáforo
const int rojo2Pin = 23;
const int amarillo2Pin = 21;
const int verde2Pin = 19;
const int boton2Pin = 34;

// Variable para almacenar el estado del botón del primer semáforo
int boton1Estado = 0;

// Variable para almacenar el estado del botón del segundo semáforo
int boton2Estado = 0;

void setup() {
  // Inicialización de pines
  pinMode(rojo1Pin, OUTPUT);
  pinMode(amarillo1Pin, OUTPUT);
  pinMode(verde1Pin, OUTPUT);
  pinMode(boton1Pin, INPUT);

  pinMode(rojo2Pin, OUTPUT);
  pinMode(amarillo2Pin, OUTPUT);
  pinMode(verde2Pin, OUTPUT);
  pinMode(boton2Pin, INPUT);
}

void loop() {
  // Leer estado del botón del primer semáforo
  boton1Estado = digitalRead(boton1Pin);

  // Si se presiona el botón del primer semáforo, cambiar color de rojo a verde
  if (boton1Estado == HIGH) {
    digitalWrite(rojo1Pin, LOW);
    digitalWrite(verde1Pin, HIGH);
    delay(5000); // Esperar 5 segundos en verde
    digitalWrite(verde1Pin, LOW);
    digitalWrite(amarillo1Pin, HIGH);
    delay(2000); // Esperar 2 segundos en amarillo
    digitalWrite(amarillo1Pin, LOW);
    digitalWrite(rojo1Pin, HIGH);
    delay(2000); // Esperar 2 segundos en rojo
  }

  // Leer estado del botón del segundo semáforo
  boton2Estado = digitalRead(boton2Pin);

  // Si se presiona el botón del segundo semáforo, cambiar color de rojo a verde
  if (boton2Estado == HIGH) {
    digitalWrite(rojo2Pin, LOW);
    digitalWrite(verde2Pin, HIGH);
    delay(5000); // Esperar 5 segundos en verde
    digitalWrite(verde2Pin, LOW);
    digitalWrite(amarillo2Pin, HIGH);
    delay(2000); // Esperar 2 segundos en amarillo
    digitalWrite(amarillo2Pin, LOW);
    digitalWrite(rojo2Pin, HIGH);
    delay(2000); // Esperar 2 segundos en rojo
  }
}

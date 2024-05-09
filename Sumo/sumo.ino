#include <AFMotor.h>

//pines para los motores (IN1, IN2, IN3, IN4)
#define IN1 11
#define IN2 10
#define IN3 9
#define IN4 8

// pines sensor ultrasónico
#define trigPin 7
#define echoPin 6

// distancia max o limite (en centímetros)
#define distanciaLimite 20

// motores nombra con el driver L298N
AF_DCMotor motor1(1); // Motor izquierdo
AF_DCMotor motor2(2); // Motor derecho

void setup() {
  //  pines de control como salidas
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  //pines del sensor ultrasónico
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // motores
  motor1.setSpeed(255); // Velocidad máxima
  motor2.setSpeed(255); // Velocidad máxima

  // Inicializa la comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Genera un pulso corto en el pin de trigger del sensor ultrasónico
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // durción del pulso de eco del sensor ultrasónico
  long duracion = pulseIn(echoPin, HIGH);

  // calcula la distancia en centímetros
  int distancia = duracion * 0.034 / 2;

  // muestra la distancia en el monitor serial
  Serial.print("Distancia: ");
  Serial.println(distancia);

  // comprobar si hay un objeto a distancia 
  if (distancia < distanciaLimite) {
    // Imprimir atacando
    Serial.println("Atacando");

    //avanzar 
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
  } else {
    // indicar si no hay objeto gira 
    Serial.println("Girando a la derecha");

    // si no hay objetivos (enemigos), gira a la derecha
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
  }

  // tiempo de lectura del monitor serial 
  delay(100);
}

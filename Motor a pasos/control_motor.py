import RPi.GPIO as GPIO
import time

class control():
    def __init__(self):
        super().__init__()
        

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#Lado 1 del motor
GPIO.setup(15, GPIO.OUT) #IN1
GPIO.setup(14, GPIO.OUT) #IN2

#lado 2 del motor
GPIO.setup(4, GPIO.OUT) #IN3
GPIO.setup(3, GPIO.OUT) #IN4

pasosPorRev = 4096



def stepDeUnLado():
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)

def stepDeotroLado():
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(3, GPIO.HIGH)

def moverAngulo(angulo, delay):
    steps = int(pasosPorRev*angulo/360)


    if angulo >= 0:
        for _ in range(steps):
            stepDeUnLado()
            time.sleep(delay)
    else:
        for _ in range(abs(steps)):
            stepDeotroLado()
            time.sleep(delay)

def limpiar():
    GPIO.cleanup()

    

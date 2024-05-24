import RPi.GPIO as GPIO

# Configuração dos pinos GPIO para os motores
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # IN1
GPIO.setup(27, GPIO.OUT)  # IN2
GPIO.setup(22, GPIO.OUT)  # IN3
GPIO.setup(23, GPIO.OUT)  # IN4

def motores_frente():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)

def motores_tras():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)

def motores_parar():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)

def virar_esquerda():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)

def virar_direita():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)

def cleanup():
    GPIO.cleanup()

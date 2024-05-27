import RPi.GPIO as GPIO
from time import sleep

# Configuração dos pinos GPIO para os motores
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pinos de controle do motor (Primeira Ponte H - Esquerda)
IN1_L = 17
IN2_L = 27
IN3_L = 22
IN4_L = 23
ENA_L = 18

# Pinos de controle do motor (Segunda Ponte H - Direita)
IN1_R = 5
IN2_R = 6
IN3_R = 13
IN4_R = 19
ENA_R = 12

# Configuração dos pinos de controle (Esquerda)
GPIO.setup(IN1_L, GPIO.OUT)
GPIO.setup(IN2_L, GPIO.OUT)
GPIO.setup(IN3_L, GPIO.OUT)
GPIO.setup(IN4_L, GPIO.OUT)
GPIO.setup(ENA_L, GPIO.OUT)

# Configuração dos pinos de controle (Direita)
GPIO.setup(IN1_R, GPIO.OUT)
GPIO.setup(IN2_R, GPIO.OUT)
GPIO.setup(IN3_R, GPIO.OUT)
GPIO.setup(IN4_R, GPIO.OUT)
GPIO.setup(ENA_R, GPIO.OUT)

# Ativar os pinos de ENA para os motores
GPIO.output(ENA_L, GPIO.HIGH)
GPIO.output(ENA_R, GPIO.HIGH)

def motores_frente():
    # Motores da esquerda
    GPIO.output(IN1_L, GPIO.HIGH)
    GPIO.output(IN2_L, GPIO.LOW)
    GPIO.output(IN3_L, GPIO.HIGH)
    GPIO.output(IN4_L, GPIO.LOW)
    
    # Motores da direita
    GPIO.output(IN1_R, GPIO.HIGH)
    GPIO.output(IN2_R, GPIO.LOW)
    GPIO.output(IN3_R, GPIO.HIGH)
    GPIO.output(IN4_R, GPIO.LOW)

def motores_parar():
    # Motores da esquerda
    GPIO.output(IN1_L, GPIO.LOW)
    GPIO.output(IN2_L, GPIO.LOW)
    GPIO.output(IN3_L, GPIO.LOW)
    GPIO.output(IN4_L, GPIO.LOW)
    
    # Motores da direita
    GPIO.output(IN1_R, GPIO.LOW)
    GPIO.output(IN2_R, GPIO.LOW)
    GPIO.output(IN3_R, GPIO.LOW)
    GPIO.output(IN4_R, GPIO.LOW)

try:
    while True:
        motores_frente()
        sleep(2)
        motores_parar()
        sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()

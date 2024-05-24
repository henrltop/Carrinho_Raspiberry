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

# Configuração dos pinos de controle (Direita)
GPIO.setup(IN1_R, GPIO.OUT)
GPIO.setup(IN2_R, GPIO.OUT)
GPIO.setup(IN3_R, GPIO.OUT)
GPIO.setup(IN4_R, GPIO.OUT)

# Configuração dos pinos de PWM
GPIO.setup(ENA_L, GPIO.OUT)
GPIO.setup(ENA_R, GPIO.OUT)

# Inicialização do PWM
pwm_l = GPIO.PWM(ENA_L, 1000)  # Frequência de 1kHz
pwm_r = GPIO.PWM(ENA_R, 1000)  # Frequência de 1kHz

pwm_l.start(0)
pwm_r.start(0)

def motores_frente(velocidade):
    # Motores da esquerda
    GPIO.output(IN1_L, GPIO.HIGH)
    GPIO.output(IN2_L, GPIO.LOW)
    GPIO.output(IN3_L, GPIO.HIGH)
    GPIO.output(IN4_L, GPIO.LOW)
    pwm_l.ChangeDutyCycle(velocidade)
    
    # Motores da direita
    GPIO.output(IN1_R, GPIO.HIGH)
    GPIO.output(IN2_R, GPIO.LOW)
    GPIO.output(IN3_R, GPIO.HIGH)
    GPIO.output(IN4_R, GPIO.LOW)
    pwm_r.ChangeDutyCycle(velocidade)

def motores_tras(velocidade):
    # Motores da esquerda
    GPIO.output(IN1_L, GPIO.LOW)
    GPIO.output(IN2_L, GPIO.HIGH)
    GPIO.output(IN3_L, GPIO.LOW)
    GPIO.output(IN4_L, GPIO.HIGH)
    pwm_l.ChangeDutyCycle(velocidade)
    
    # Motores da direita
    GPIO.output(IN1_R, GPIO.LOW)
    GPIO.output(IN2_R, GPIO.HIGH)
    GPIO.output(IN3_R, GPIO.LOW)
    GPIO.output(IN4_R, GPIO.HIGH)
    pwm_r.ChangeDutyCycle(velocidade)

def motores_parar():
    # Motores da esquerda
    GPIO.output(IN1_L, GPIO.LOW)
    GPIO.output(IN2_L, GPIO.LOW)
    GPIO.output(IN3_L, GPIO.LOW)
    GPIO.output(IN4_L, GPIO.LOW)
    pwm_l.ChangeDutyCycle(0)
    
    # Motores da direita
    GPIO.output(IN1_R, GPIO.LOW)
    GPIO.output(IN2_R, GPIO.LOW)
    GPIO.output(IN3_R, GPIO.LOW)
    GPIO.output(IN4_R, GPIO.LOW)
    pwm_r.ChangeDutyCycle(0)

def virar_esquerda(velocidade):
    # Motores da esquerda para trás
    GPIO.output(IN1_L, GPIO.LOW)
    GPIO.output(IN2_L, GPIO.HIGH)
    GPIO.output(IN3_L, GPIO.LOW)
    GPIO.output(IN4_L, GPIO.HIGH)
    pwm_l.ChangeDutyCycle(velocidade)
    
    # Motores da direita para frente
    GPIO.output(IN1_R, GPIO.HIGH)
    GPIO.output(IN2_R, GPIO.LOW)
    GPIO.output(IN3_R, GPIO.HIGH)
    GPIO.output(IN4_R, GPIO.LOW)
    pwm_r.ChangeDutyCycle(velocidade)

def virar_direita(velocidade):
    # Motores da esquerda para frente
    GPIO.output(IN1_L, GPIO.HIGH)
    GPIO.output(IN2_L, GPIO.LOW)
    GPIO.output(IN3_L, GPIO.HIGH)
    GPIO.output(IN4_L, GPIO.LOW)
    pwm_l.ChangeDutyCycle(velocidade)
    
    # Motores da direita para trás
    GPIO.output(IN1_R, GPIO.LOW)
    GPIO.output(IN2_R, GPIO.HIGH)
    GPIO.output(IN3_R, GPIO.LOW)
    GPIO.output(IN4_R, GPIO.HIGH)
    pwm_r.ChangeDutyCycle(velocidade)

def cleanup():
    pwm_l.stop()
    pwm_r.stop()
    GPIO.cleanup()

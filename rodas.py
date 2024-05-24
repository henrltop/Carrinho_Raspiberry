import RPi.GPIO as GPIO
from time import sleep

# Configuração dos pinos GPIO para os motores
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pinos de controle do motor
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

# Pinos de PWM
ENA = 18
ENB = 19

# Configuração dos pinos de controle
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Configuração dos pinos de PWM
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# Inicialização do PWM
pwm_a = GPIO.PWM(ENA, 1000)  # Frequência de 1kHz
pwm_b = GPIO.PWM(ENB, 1000)  # Frequência de 1kHz

pwm_a.start(0)
pwm_b.start(0)

def motores_frente(velocidade):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_a.ChangeDutyCycle(velocidade)
    pwm_b.ChangeDutyCycle(velocidade)

def motores_tras(velocidade):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(velocidade)
    pwm_b.ChangeDutyCycle(velocidade)

def motores_parar():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

def virar_esquerda(velocidade):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_a.ChangeDutyCycle(velocidade)
    pwm_b.ChangeDutyCycle(velocidade)

def virar_direita(velocidade):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_a.ChangeDutyCycle(velocidade)
    pwm_b.ChangeDutyCycle(velocidade)

def cleanup():
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()

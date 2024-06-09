import RPi.GPIO as GPIO
import pygame
from time import sleep

# Configuração dos pinos GPIO para os motores
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pinos de controle do motor (Primeira Ponte H - Esquerda)
IN1_LF = 17  # Motor Esquerdo Dianteiro
IN2_LF = 27  # Motor Esquerdo Dianteiro
IN1_LR = 22  # Motor Esquerdo Traseiro
IN2_LR = 23  # Motor Esquerdo Traseiro
ENA_LF = 18  # PWM Motor Esquerdo Dianteiro
ENB_LR = 19  # PWM Motor Esquerdo Traseiro

# Pinos de controle do motor (Segunda Ponte H - Direita)
IN1_RF = 5   # Motor Direito Dianteiro
IN2_RF = 6   # Motor Direito Dianteiro
IN1_RR = 13  # Motor Direito Traseiro
IN2_RR = 26  # Motor Direito Traseiro
ENA_RF = 12  # PWM Motor Direito Dianteiro
ENB_RR = 21  # PWM Motor Direito Traseiro

# Configuração dos pinos de controle (Esquerda)
GPIO.setup(IN1_LF, GPIO.OUT)
GPIO.setup(IN2_LF, GPIO.OUT)
GPIO.setup(IN1_LR, GPIO.OUT)
GPIO.setup(IN2_LR, GPIO.OUT)
GPIO.setup(ENA_LF, GPIO.OUT)
GPIO.setup(ENB_LR, GPIO.OUT)

# Configuração dos pinos de controle (Direita)
GPIO.setup(IN1_RF, GPIO.OUT)
GPIO.setup(IN2_RF, GPIO.OUT)
GPIO.setup(IN1_RR, GPIO.OUT)
GPIO.setup(IN2_RR, GPIO.OUT)
GPIO.setup(ENA_RF, GPIO.OUT)
GPIO.setup(ENB_RR, GPIO.OUT)

# Inicializar PWM nos pinos ENA e ENB
pwm_lf = GPIO.PWM(ENA_LF, 1000)  # Frequência de 1kHz
pwm_lr = GPIO.PWM(ENB_LR, 1000)  # Frequência de 1kHz
pwm_rf = GPIO.PWM(ENA_RF, 1000)  # Frequência de 1kHz
pwm_rr = GPIO.PWM(ENB_RR, 1000)  # Frequência de 1kHz
pwm_lf.start(0)
pwm_lr.start(0)
pwm_rf.start(0)
pwm_rr.start(0)

def motores_frente(velocidade):
    print("Motores para frente...")

    # Configurar velocidade
    pwm_lf.ChangeDutyCycle(velocidade)
    pwm_lr.ChangeDutyCycle(velocidade)
    pwm_rf.ChangeDutyCycle(velocidade)
    pwm_rr.ChangeDutyCycle(velocidade)

    # Motores da esquerda
    GPIO.output(IN1_LF, GPIO.HIGH)
    GPIO.output(IN2_LF, GPIO.LOW)
    GPIO.output(IN1_LR, GPIO.HIGH)
    GPIO.output(IN2_LR, GPIO.LOW)
    
    # Motores da direita
    GPIO.output(IN1_RF, GPIO.HIGH)
    GPIO.output(IN2_RF, GPIO.LOW)
    GPIO.output(IN1_RR, GPIO.HIGH)
    GPIO.output(IN2_RR, GPIO.LOW)

def motores_tras(velocidade):
    print("Motores para trás...")

    # Configurar velocidade
    pwm_lf.ChangeDutyCycle(velocidade)
    pwm_lr.ChangeDutyCycle(velocidade)
    pwm_rf.ChangeDutyCycle(velocidade)
    pwm_rr.ChangeDutyCycle(velocidade)

    # Motores da esquerda
    GPIO.output(IN1_LF, GPIO.LOW)
    GPIO.output(IN2_LF, GPIO.HIGH)
    GPIO.output(IN1_LR, GPIO.LOW)
    GPIO.output(IN2_LR, GPIO.HIGH)
    
    # Motores da direita
    GPIO.output(IN1_RF, GPIO.LOW)
    GPIO.output(IN2_RF, GPIO.HIGH)
    GPIO.output(IN1_RR, GPIO.LOW)
    GPIO.output(IN2_RR, GPIO.HIGH)

def motores_parar():
    print("Parando motores...")
    pwm_lf.ChangeDutyCycle(0)
    pwm_lr.ChangeDutyCycle(0)
    pwm_rf.ChangeDutyCycle(0)
    pwm_rr.ChangeDutyCycle(0)

    # Motores da esquerda
    GPIO.output(IN1_LF, GPIO.LOW)
    GPIO.output(IN2_LF, GPIO.LOW)
    GPIO.output(IN1_LR, GPIO.LOW)
    GPIO.output(IN2_LR, GPIO.LOW)
    
    # Motores da direita
    GPIO.output(IN1_RF, GPIO.LOW)
    GPIO.output(IN2_RF, GPIO.LOW)
    GPIO.output(IN1_RR, GPIO.LOW)
    GPIO.output(IN2_RR, GPIO.LOW)

def virar_esquerda(velocidade):
    print("Virando para a esquerda...")

    # Configurar velocidade
    pwm_lf.ChangeDutyCycle(velocidade)
    pwm_lr.ChangeDutyCycle(velocidade)
    pwm_rf.ChangeDutyCycle(velocidade)
    pwm_rr.ChangeDutyCycle(velocidade)

    # Motores da esquerda para trás
    GPIO.output(IN1_LF, GPIO.LOW)
    GPIO.output(IN2_LF, GPIO.HIGH)
    GPIO.output(IN1_LR, GPIO.LOW)
    GPIO.output(IN2_LR, GPIO.HIGH)
    
    # Motores da direita para frente
    GPIO.output(IN1_RF, GPIO.HIGH)
    GPIO.output(IN2_RF, GPIO.LOW)
    GPIO.output(IN1_RR, GPIO.HIGH)
    GPIO.output(IN2_RR, GPIO.LOW)

def virar_direita(velocidade):
    print("Virando para a direita...")

    # Configurar velocidade
    pwm_lf.ChangeDutyCycle(velocidade)
    pwm_lr.ChangeDutyCycle(velocidade)
    pwm_rf.ChangeDutyCycle(velocidade)
    pwm_rr.ChangeDutyCycle(velocidade)

    # Motores da esquerda para frente
    GPIO.output(IN1_LF, GPIO.HIGH)
    GPIO.output(IN2_LF, GPIO.LOW)
    GPIO.output(IN1_LR, GPIO.HIGH)
    GPIO.output(IN2_LR, GPIO.LOW)
    
    # Motores da direita para trás
    GPIO.output(IN1_RF, GPIO.LOW)
    GPIO.output(IN2_RF, GPIO.HIGH)
    GPIO.output(IN1_RR, GPIO.LOW)
    GPIO.output(IN2_RR, GPIO.HIGH)

def cleanup():
    print("Limpando GPIO...")
    pwm_lf.stop()
    pwm_lr.stop()
    pwm_rf.stop()
    pwm_rr.stop()
    GPIO.cleanup()

# Inicialização do Pygame para capturar eventos do joystick
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                axis_1 = joystick.get_axis(1)  # Eixo vertical do joystick esquerdo
                axis_3 = joystick.get_axis(3)  # Eixo vertical do joystick direito

                # Mapear valores do joystick (-1 a 1) para duty cycle PWM (0 a 100)
                velocidade_frente_tras = int((abs(axis_1) * 100))
                velocidade_esquerda_direita = int((abs(axis_3) * 100))

                if axis_1 < -0.1:
                    motores_frente(velocidade_frente_tras)
                elif axis_1 > 0.1:
                    motores_tras(velocidade_frente_tras)
                else:
                    motores_parar()

                if axis_3 < -0.1:
                    virar_esquerda(velocidade_esquerda_direita)
                elif axis_3 > 0.1:
                    virar_direita(velocidade_esquerda_direita)
                else:
                    motores_parar()

except KeyboardInterrupt:
    cleanup()

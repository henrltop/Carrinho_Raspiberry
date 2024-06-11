import RPi.GPIO as GPIO

# Configurações dos pinos GPIO conforme o mapeamento fornecido
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor Esquerdo Dianteiro
IN1_LF = 17
IN2_LF = 27
ENA_LF = 18

# Motor Esquerdo Traseiro
IN1_LR = 22
IN2_LR = 23
ENB_LR = 19

# Motor Direito Dianteiro
IN1_RF = 5
IN2_RF = 6
ENA_RF = 12

# Motor Direito Traseiro
IN1_RR = 13
IN2_RR = 26
ENB_RR = 21

GPIO.setup([IN1_LF, IN2_LF, ENA_LF, IN1_LR, IN2_LR, ENB_LR, IN1_RF, IN2_RF, ENA_RF, IN1_RR, IN2_RR, ENB_RR], GPIO.OUT)

pwm_lf = GPIO.PWM(ENA_LF, 1000)
pwm_lr = GPIO.PWM(ENB_LR, 1000)
pwm_rf = GPIO.PWM(ENA_RF, 1000)
pwm_rr = GPIO.PWM(ENB_RR, 1000)

pwm_lf.start(0)
pwm_lr.start(0)
pwm_rf.start(0)
pwm_rr.start(0)

def motores_frente(velocidade):
    if 0 <= velocidade <= 100:
        print(f"Motores para frente com velocidade {velocidade}")
        pwm_lf.ChangeDutyCycle(velocidade)
        pwm_lr.ChangeDutyCycle(velocidade)
        pwm_rf.ChangeDutyCycle(velocidade)
        pwm_rr.ChangeDutyCycle(velocidade)

        GPIO.output(IN1_LF, GPIO.HIGH)
        GPIO.output(IN2_LF, GPIO.LOW)
        GPIO.output(IN1_LR, GPIO.HIGH)
        GPIO.output(IN2_LR, GPIO.LOW)
        GPIO.output(IN1_RF, GPIO.HIGH)
        GPIO.output(IN2_RF, GPIO.LOW)
        GPIO.output(IN1_RR, GPIO.HIGH)
        GPIO.output(IN2_RR, GPIO.LOW)
    else:
        print(f"Velocidade inválida: {velocidade}")

def motores_tras(velocidade):
    if 0 <= velocidade <= 100:
        print(f"Motores para trás com velocidade {velocidade}")
        pwm_lf.ChangeDutyCycle(velocidade)
        pwm_lr.ChangeDutyCycle(velocidade)
        pwm_rf.ChangeDutyCycle(velocidade)
        pwm_rr.ChangeDutyCycle(velocidade)

        GPIO.output(IN1_LF, GPIO.LOW)
        GPIO.output(IN2_LF, GPIO.HIGH)
        GPIO.output(IN1_LR, GPIO.LOW)
        GPIO.output(IN2_LR, GPIO.HIGH)
        GPIO.output(IN1_RF, GPIO.LOW)
        GPIO.output(IN2_RF, GPIO.HIGH)
        GPIO.output(IN1_RR, GPIO.LOW)
        GPIO.output(IN2_RR, GPIO.HIGH)
    else:
        print(f"Velocidade inválida: {velocidade}")

def virar_esquerda(velocidade):
    if 0 <= velocidade <= 100:
        print(f"Virando à esquerda com velocidade {velocidade}")
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
    else:
        print(f"Velocidade inválida: {velocidade}")

def virar_direita(velocidade):
    if 0 <= velocidade <= 100:
        print(f"Virando à direita com velocidade {velocidade}")
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
    else:
        print(f"Velocidade inválida: {velocidade}")

def motores_parar():
    print("Parando motores")
    pwm_lf.ChangeDutyCycle(0)
    pwm_lr.ChangeDutyCycle(0)
    pwm_rf.ChangeDutyCycle(0)
    pwm_rr.ChangeDutyCycle(0)

def cleanup():
    print("Limpando GPIO...")
    pwm_lf.stop()
    pwm_lr.stop()
    pwm_rf.stop()
    pwm_rr.stop()
    GPIO.cleanup()

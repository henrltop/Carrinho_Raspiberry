import RPi.GPIO as GPIO

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

def set_speed(velocidade):
    print(f"Setando velocidade para {velocidade}%")
    pwm_lf.ChangeDutyCycle(velocidade)
    pwm_lr.ChangeDutyCycle(velocidade)
    pwm_rf.ChangeDutyCycle(velocidade)
    pwm_rr.ChangeDutyCycle(velocidade)

def cleanup():
    print("Limpando GPIO...")
    pwm_lf.stop()
    pwm_lr.stop()
    pwm_rf.stop()
    pwm_rr.stop()
    GPIO.cleanup()

import pygame
import sys
from rodas import motores_frente, motores_parar, cleanup
from camera import tirar_foto, iniciar_gravacao, parar_gravacao
from truques import volta_360
from time import sleep

# Inicializa o Pygame
pygame.init()

# Inicializa os joysticks
pygame.joystick.init()

# Verifica se há joysticks conectados
if pygame.joystick.get_count() == 0:
    print("Nenhum controle conectado.")
    pygame.quit()
    sys.exit()

# Pega o primeiro joystick conectado
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Controle detectado: {joystick.get_name()}")

# Mapear botões
BUTTON_X = 2
BUTTON_O = 1
BUTTON_TRIANGLE = 0
BUTTON_SQUARE = 3
BUTTON_L1 = 4
BUTTON_L2 = 6
BUTTON_R1 = 5
BUTTON_R2 = 7

# Variável para armazenar a velocidade atual
velocidade_atual = 0

# Função para aumentar a velocidade
def aumentar_velocidade():
    global velocidade_atual
    if velocidade_atual < 100:
        velocidade_atual += 10
        if velocidade_atual > 100:
            velocidade_atual = 100
        print(f"Aumentando velocidade para {velocidade_atual}")
        motores_frente(velocidade_atual)
    else:
        print("Velocidade máxima atingida")

# Loop principal
try:
    recording = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(BUTTON_X):
                    tirar_foto()
                elif joystick.get_button(BUTTON_O):
                    if not recording:
                        iniciar_gravacao()
                        recording = True
                    else:
                        parar_gravacao()
                        recording = False
                elif joystick.get_button(BUTTON_TRIANGLE):
                    volta_360()
                elif joystick.get_button(BUTTON_R2):
                    while joystick.get_button(BUTTON_R2):
                        aumentar_velocidade()
                        sleep(0.5)  # Incremento a cada 0.5 segundos

            if event.type == pygame.JOYBUTTONUP:
                if event.button == BUTTON_R2:
                    print("Parando motores - botão R2 liberado")
                    motores_parar()
                    velocidade_atual = 0

except KeyboardInterrupt:
    cleanup()

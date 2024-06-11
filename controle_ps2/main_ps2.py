import pygame
import sys
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
from camera import tirar_foto, iniciar_gravacao, parar_gravacao
from truques import volta_360

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
            
            if event.type == pygame.JOYAXISMOTION:
                axis_1 = joystick.get_axis(1)  # Eixo vertical do joystick esquerdo
                axis_3 = joystick.get_axis(3)  # Eixo vertical do joystick direito

                # Mapear valores do joystick (-1 a 1) para duty cycle PWM (0 a 100)
                velocidade_frente_tras = int((abs(axis_1) * 100))
                velocidade_esquerda_direita = int((abs(axis_3) * 100))

                if axis_1 < -0.1:
                    print(f"Movendo para frente com velocidade {velocidade_frente_tras}")
                    motores_frente(velocidade_frente_tras)
                elif axis_1 > 0.1:
                    print(f"Movendo para trás com velocidade {velocidade_frente_tras}")
                    motores_tras(velocidade_frente_tras)
                else:
                    motores_parar()

                if axis_3 < -0.1:
                    print(f"Virando à esquerda com velocidade {velocidade_esquerda_direita}")
                    virar_esquerda(velocidade_esquerda_direita)
                elif axis_3 > 0.1:
                    print(f"Virando à direita com velocidade {velocidade_esquerda_direita}")
                    virar_direita(velocidade_esquerda_direita)
                else:
                    motores_parar()

except KeyboardInterrupt:
    cleanup()

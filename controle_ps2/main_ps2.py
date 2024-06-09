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

# Mapeamento dos botões do controle PS2
BUTTON_TRIANGLE = 0
BUTTON_CIRCLE = 1
BUTTON_X = 2
BUTTON_SQUARE = 3
BUTTON_L1 = 4
BUTTON_R1 = 5
BUTTON_L2 = 6
BUTTON_R2 = 7

# Função para acelerar gradualmente
def acelerar_gradualmente():
    velocidade = 0.1  # 10% da velocidade máxima
    incremento = 0.1  # Incremento de 10%
    max_velocidade = 1.0  # 100% da velocidade máxima

    while velocidade < max_velocidade:
        motores_frente(int(velocidade * 100))  # Definir velocidade em percentual
        velocidade += incremento
        pygame.time.wait(500)  # Espera 0.5 segundos antes de incrementar a velocidade
    motores_frente(int(max_velocidade * 100))

# Loop principal
running = True
gravando_video = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == BUTTON_R2:
                acelerar_gradualmente()
            elif event.button == BUTTON_L1:
                tirar_foto()
            elif event.button == BUTTON_TRIANGLE:
                if not gravando_video:
                    iniciar_gravacao()
                    gravando_video = True
                else:
                    parar_gravacao()
                    gravando_video = False
            elif event.button == BUTTON_CIRCLE:
                volta_360()
        elif event.type == pygame.JOYAXISMOTION:
            axis_0 = joystick.get_axis(0)
            axis_3 = joystick.get_axis(3)
            
            velocidade = int((abs(axis_3) * 100))
            if axis_3 < -0.1:
                motores_frente(velocidade)
            elif axis_3 > 0.1:
                motores_tras(velocidade)
            else:
                motores_parar()
            
            if axis_0 < -0.1:
                virar_esquerda()
            elif axis_0 > 0.1:
                virar_direita()
            else:
                motores_parar()

# Encerra o Pygame
pygame.quit()
cleanup()
sys.exit()

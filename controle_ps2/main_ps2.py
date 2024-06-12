import pygame
import sys
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
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
BUTTON_L2 = 6  # Gatilho esquerdo para alternar direção
BUTTON_R1 = 5  # Botão em cima do gatilho direito
BUTTON_R2 = 7  # Gatilho direito para andar

# Variável para armazenar a velocidade atual
velocidade_atual = 0

# Variável para armazenar o estado do modo de ré
modo_re = False

# Função para aumentar a velocidade
def aumentar_velocidade():
    global velocidade_atual
    if velocidade_atual < 100:
        velocidade_atual += 10
        if velocidade_atual > 100:
            velocidade_atual = 100
        print(f"Aumentando velocidade para {velocidade_atual}")

# Função para diminuir a velocidade
def diminuir_velocidade():
    global velocidade_atual
    if velocidade_atual > 0:
        velocidade_atual -= 10
        if velocidade_atual < 0:
            velocidade_atual = 0
        print(f"Diminuindo velocidade para {velocidade_atual}")

# Função para alternar o modo de ré
def alternar_modo_re():
    global modo_re
    motores_parar()
    print("Parando motores para alternar direção")
    sleep(1)  # Espera 1 segundo para garantir que os motores parem completamente
    modo_re = not modo_re
    if modo_re:
        print("Modo de ré ativado")
    else:
        print("Modo de ré desativado")

# Função para parar completamente
def parar_completamente():
    global velocidade_atual
    velocidade_atual = 0
    print("Parando completamente")
    motores_parar()

# Função para controlar movimento
def controlar_movimento():
    if modo_re:
        motores_tras(velocidade_atual)
    else:
        motores_frente(velocidade_atual)

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
                elif joystick.get_button(BUTTON_R1):  # Botão em cima do gatilho direito
                    aumentar_velocidade()
                elif joystick.get_button(BUTTON_L1):  # Botão em cima do gatilho esquerdo
                    diminuir_velocidade()
                elif joystick.get_button(BUTTON_L2):  # Gatilho esquerdo
                    alternar_modo_re()
                elif joystick.get_button(BUTTON_SQUARE):  # Botão Quadrado
                    parar_completamente()

        try:
            axis_0 = joystick.get_axis(0)  # Eixo horizontal do joystick esquerdo
            print(f"Eixo horizontal (axis_0): {axis_0}")
            r2_pressed = joystick.get_button(BUTTON_R2)  # Verifica se o gatilho direito está pressionado
            print(f"Gatilho direito (BUTTON_R2): {r2_pressed}")

            # Verificar se o gatilho direito está pressionado
            if r2_pressed:
                if axis_0 < -0.1:
                    velocidade_curva = int(abs(axis_0) * velocidade_atual)
                    print(f"Virando à esquerda com velocidade {velocidade_curva}")
                    virar_esquerda(velocidade_curva)
                elif axis_0 > 0.1:
                    velocidade_curva = int(abs(axis_0) * velocidade_atual)
                    print(f"Virando à direita com velocidade {velocidade_curva}")
                    virar_direita(velocidade_curva)
                else:
                    controlar_movimento()
            else:
                motores_parar()
        except pygame.error as e:
            print(f"Erro ao ler o joystick: {e}")

except KeyboardInterrupt:
    cleanup()

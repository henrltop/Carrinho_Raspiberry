import cv2
from datetime import datetime
import os

# Função para criar diretório se não existir
def criar_diretorio_se_nao_existir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

# Função para tirar uma foto
def tirar_foto():
    diretorio = '/home/fab/Imagens'
    criar_diretorio_se_nao_existir(diretorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(diretorio, f'image_{timestamp}.jpg')

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(file_path, frame)
        print(f"Foto salva como {file_path}")
    cap.release()

# Função para iniciar gravação de vídeo
def iniciar_gravacao():
    diretorio = '/home/fab/Vídeos'
    criar_diretorio_se_nao_existir(diretorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(diretorio, f'video_{timestamp}.mp4')

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para mp4
    out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

    print(f"Gravação iniciada: {file_path}")
    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Use 'q' para parar a gravação
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Gravação parada")

# Função para parar a gravação
def parar_gravacao():
    # Esta função não é necessária pois a gravação já é parada com 'q' na função iniciar_gravacao
    pass

# Função para fechar a câmera
def fechar_camera():
    # Esta função não é necessária com o OpenCV, pois a câmera é liberada diretamente nas funções
    pass

# Inicializa o Pygame e o joystick
import pygame
import sys
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
from truques import volta_360
from time import sleep

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle conectado.")
    pygame.quit()
    sys.exit()

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

        axis_0 = joystick.get_axis(0)  # Eixo horizontal do joystick esquerdo
        r2_pressed = joystick.get_button(BUTTON_R2)  # Verifica se o gatilho direito está pressionado

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

except KeyboardInterrupt:
    cleanup()

import pygame
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, volta_360, cleanup
from camera import tirar_foto, iniciar_gravacao, parar_gravacao, fechar_camera

# Inicializar o pygame
pygame.init()

# Inicializar o joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

gravando = False
arquivo_video = None

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Eixo 0 (esquerda/direita)
                axis_0 = joystick.get_axis(0)
                
                # Lógica para controle proporcional do carrinho
                if axis_0 < -0.1:
                    virar_esquerda()
                elif axis_0 > 0.1:
                    virar_direita()
                else:
                    motores_parar()

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 8:  # Botão RT
                    motores_frente()
                if event.button == 2:  # Botão X para tirar foto
                    tirar_foto()
                if event.button == 6:  # Botão RB para fazer uma volta de 360 graus
                    volta_360()
                if event.button == 0:  # Botão A para iniciar/parar gravação
                    if not gravando:
                        arquivo_video = iniciar_gravacao()
                        gravando = True
                    else:
                        parar_gravacao()
                        gravando = False

            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 8:  # Botão RT
                    motores_parar()

except KeyboardInterrupt:
    cleanup()
    fechar_camera()
    pygame.quit()

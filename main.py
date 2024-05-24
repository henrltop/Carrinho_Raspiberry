import pygame
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
from camera import tirar_foto, iniciar_gravacao, parar_gravacao, fechar_camera
from truques import volta_360

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
                # Eixo 0 (esquerda/direita) do joystick esquerdo para rotação
                axis_0 = joystick.get_axis(0)
                # Eixo 3 (cima/baixo) do joystick direito para aceleração
                axis_3 = joystick.get_axis(3)
                
                # Controle da velocidade com o joystick direito
                velocidade = int((abs(axis_3) * 100))

                # Controle do movimento
                if axis_3 < -0.1:
                    motores_frente(velocidade)
                elif axis_3 > 0.1:
                    motores_tras(velocidade)
                else:
                    motores_parar()
                
                # Controle da direção com o joystick esquerdo
                if axis_0 < -0.1:
                    virar_esquerda(velocidade)
                elif axis_0 > 0.1:
                    virar_direita(velocidade)

            elif event.type == pygame.JOYBUTTONDOWN:
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

except KeyboardInterrupt:
    cleanup()
    fechar_camera()
    pygame.quit()

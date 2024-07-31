###############################################################################
#                                                                             #
#                        Projeto: Rover com Raspberry Pi                      #
#                        Autor: Henrique Cunha                                #
#                        Data: 20/05/2024                                     #
#                                                                             #
###############################################################################

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
                # Eixo 0 (esquerda/direita) do joystick esquerdo para controle de direção
                axis_0 = joystick.get_axis(0)
                # Eixo 1 (frente/trás) do joystick esquerdo para controle de movimento
                axis_1 = joystick.get_axis(1)
                # Eixo 2 (esquerda/direita) do joystick direito para controle de direção
                axis_2 = joystick.get_axis(2)
                # Eixo 4 (RT) para controle de velocidade
                axis_4 = joystick.get_axis(4)

                # Controle da velocidade com o gatilho direito (RT)
                velocidade = int((axis_4 + 1) * 50)  # RT varia de -1 a 1, ajuste para variar de 0 a 100
                print(velocidade)

                # Controle do movimento frente/trás com o joystick esquerdo
                if axis_1 < -0.1:
                    print("Movendo para frente")
                    motores_frente(velocidade)
                elif axis_1 > 0.1:
                    print("Movendo para trás")
                    motores_tras(velocidade)
                else:
                    motores_parar()

                # Controle da direção com o joystick direito
                if axis_2 < -0.1:
                    print("Virando à esquerda")
                    virar_esquerda(velocidade)
                elif axis_2 > 0.1:
                    print("Virando à direita")
                    virar_direita(velocidade)

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 2:  # Botão X para tirar foto
                    print("Tirando foto")
                    tirar_foto()
                if event.button == 6:  # Botão RB para fazer uma volta de 360 graus
                    print("Realizando volta de 360 graus")
                    volta_360()
                if event.button == 0:  # Botão A para iniciar/parar gravação
                    if not gravando:
                        print("Iniciando gravação")
                        arquivo_video = iniciar_gravacao()
                        gravando = True
                    else:
                        print("Parando gravação")
                        parar_gravacao()
                        gravando = False

except KeyboardInterrupt:
    cleanup()
    fechar_camera()
    pygame.quit()

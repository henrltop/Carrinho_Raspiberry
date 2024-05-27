import pygame
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
from truques import volta_360

# Inicializar o pygame
pygame.init()

# Inicializar o joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Variável para controle de gravação
gravando = False

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Eixo 0 (esquerda/direita) do joystick esquerdo para rotação
                axis_0 = joystick.get_axis(0)
                # Eixo 3 (cima/baixo) do joystick direito para aceleração
                axis_3 = joystick.get_axis(3)

                # Controle do movimento
                if axis_3 < -0.1:
                    print("Movendo para frente")
                    motores_frente()
                elif axis_3 > 0.1:
                    print("Movendo para trás")
                    motores_tras()
                else:
                    print("Parando")
                    motores_parar()
                
                # Controle da direção com o joystick esquerdo
                if axis_0 < -0.1:
                    print("Virando à esquerda")
                    virar_esquerda()
                elif axis_0 > 0.1:
                    print("Virando à direita")
                    virar_direita()
                else:
                    motores_parar()

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6:  # Botão RB para fazer uma volta de 360 graus
                    print("Realizando volta de 360 graus")
                    volta_360()
                elif event.button == 0:  # Botão A para iniciar/parar gravação
                    if not gravando:
                        print("Iniciando gravação")
                        arquivo_video = iniciar_gravacao()
                        gravando = True
                    else:
                        print("Parando gravação")
                        parar_gravacao()
                        gravando = False
                elif event.button == 2:  # Botão X para tirar foto
                    print("Tirando foto")
                    tirar_foto()

except KeyboardInterrupt:
    cleanup()
    pygame.quit()

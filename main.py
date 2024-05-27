import pygame
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
from camera import tirar_foto, iniciar_gravacao, parar_gravacao, fechar_camera
from truques import volta_360

# Inicializar o pygame
print("Inicializando pygame...")
pygame.init()

# Inicializar o joystick
print("Inicializando joystick...")
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
                # Eixo 1 (cima/baixo) do joystick esquerdo para direção
                axis_1 = joystick.get_axis(1)
                # Eixo 3 (cima/baixo) do joystick direito para aceleração
                axis_3 = joystick.get_axis(3)
                
                # Controle da velocidade com o joystick direito
                velocidade = int((abs(axis_3) * 100))
                print(f"Velocidade: {velocidade}")

                # Controle do movimento
                if axis_3 < -0.1:
                    print("Movendo para frente...")
                    motores_frente(velocidade)
                elif axis_3 > 0.1:
                    print("Movendo para trás...")
                    motores_tras(velocidade)
                else:
                    print("Parando motores...")
                    motores_parar()
                
                # Controle da direção com o joystick esquerdo
                if axis_0 < -0.1:
                    print("Virando para a esquerda...")
                    virar_esquerda(velocidade)
                elif axis_0 > 0.1:
                    print("Virando para a direita...")
                    virar_direita(velocidade)
                else:
                    motores_parar()

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 2:  # Botão X para tirar foto
                    print("Tirando foto...")
                    tirar_foto()
                if event.button == 6:  # Botão RB para fazer uma volta de 360 graus
                    print("Executando volta de 360 graus...")
                    volta_360()
                if event.button == 0:  # Botão A para iniciar/parar gravação
                    if not gravando:
                        print("Iniciando gravação...")
                        arquivo_video = iniciar_gravacao()
                        gravando = True
                    else:
                        print("Parando gravação...")
                        parar_gravacao()
                        gravando = False

except KeyboardInterrupt:
    print("Interrupção detectada. Limpando GPIO e fechando câmera...")
    cleanup()
    fechar_camera()
    pygame.quit()

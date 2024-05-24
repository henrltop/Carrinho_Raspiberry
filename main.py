import pygame
from rodas import motores_frente, motores_tras, motores_parar, virar_esquerda, virar_direita, cleanup
from camera import tirar_foto, fechar_camera

# Inicializar o pygame
pygame.init()

# Inicializar o joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

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
                if event.button == 8:
                    motores_frente()
                if event.button == 2:  # Botão 2 para tirar foto
                    tirar_foto()

            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 8:
                    motores_parar()

except KeyboardInterrupt:
    cleanup()
    fechar_camera()
    pygame.quit()

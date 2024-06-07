import pygame

pygame.init()

# Inicializar o joystick
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum joystick detectado.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick detectado: {joystick.get_name()}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value
                print(f"Eixo {axis} movido: {value}")

            if event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print(f"Botão {button} pressionado")

            if event.type == pygame.JOYBUTTONUP:
                button = event.button
                print(f"Botão {button} solto")

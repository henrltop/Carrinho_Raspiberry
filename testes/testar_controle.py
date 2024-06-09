import pygame
import sys

def main():
    # Inicializa o Pygame
    pygame.init()

    # Inicializa os joysticks
    pygame.joystick.init()

    # Verifica se há joysticks conectados
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("Nenhum controle conectado.")
        pygame.quit()
        sys.exit()

    # Pega o primeiro joystick conectado
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Controle detectado: {joystick.get_name()}")

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Botão pressionado: {event.button}")
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Eixo {event.axis} valor: {event.value:.2f}")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} valor: {event.value}")

    # Encerra o Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

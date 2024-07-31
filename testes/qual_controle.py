import pygame

pygame.init()
pygame.joystick.init()

# Conta quantos joysticks estão conectados
num_joysticks = pygame.joystick.get_count()
print(f'Número de joysticks conectados: {num_joysticks}')

# Lista todos os joysticks detectados
for i in range(num_joysticks):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print(f'Joystick {i}: {joystick.get_name()}')
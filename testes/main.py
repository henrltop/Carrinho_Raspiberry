###############################################################################
#                                                                             #
#                        Projeto: Rover com Raspberry Pi                      #
#                        Autor: Henrique (aka Henritop)                       #
#                        Data: 20/05/2024                                     #
#                                                                             #
###############################################################################

import pygame
from rodas import set_speed, cleanup

# Inicializar o pygame
pygame.init()

# Dicionário para mapear teclas a porcentagens de velocidade
tecla_para_velocidade = {
    pygame.K_1: 10,
    pygame.K_2: 20,
    pygame.K_3: 30,
    pygame.K_4: 40,
    pygame.K_5: 50,
    pygame.K_6: 60,
    pygame.K_7: 70,
    pygame.K_8: 80,
    pygame.K_9: 90,
    pygame.K_0: 100
}

# Variável para armazenar a velocidade atual
velocidade_atual = 0

# Loop principal
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in tecla_para_velocidade:
                    velocidade_atual = tecla_para_velocidade[event.key]
                    print(f'Setando velocidade para {velocidade_atual}%')
                    set_speed(velocidade_atual)

except KeyboardInterrupt:
    pass
finally:
    cleanup()
    pygame.quit()

import pygame
import subprocess
import time

def is_controller_connected(mac_address):
    result = subprocess.run(['hcitool', 'con'], stdout=subprocess.PIPE, text=True)
    return mac_address in result.stdout

def wait_for_controller(mac_address):
    print("Aguardando conexão do controle...")
    while not is_controller_connected(mac_address):
        print("Controle não conectado, tentando novamente em 5 segundos...")
        time.sleep(5)
    print("Controle conectado!")

def main():
    mac_address = "7C:66:EF:45:C5:CB"  # Substitua pelo endereço MAC do seu controle

    wait_for_controller(mac_address)

    pygame.init()

    # Inicializar o joystick
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    print(f"Número de joysticks detectados: {joystick_count}")

    if joystick_count == 0:
        print("Nenhum joystick detectado.")
    else:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick detectado: {joystick.get_name()}")

        running = True
        while running:
            try:
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

                time.sleep(0.1)
            except KeyboardInterrupt:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()

from rodas import virar_direita, motores_parar
from time import sleep

def volta_360():
    velocidade = 100  # Velocidade máxima
    print("Realizando volta de 360 graus")
    virar_direita(velocidade)
    sleep(2)  # Ajuste o tempo conforme necessário para completar a volta
    motores_parar()

from rodas import virar_direita, motores_parar
from time import sleep

def volta_360():
    virar_direita(100)  # Velocidade máxima
    sleep(2)  # Ajuste o tempo conforme necessário para uma rotação completa
    motores_parar()

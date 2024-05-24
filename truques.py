import RPi.GPIO as GPIO
from rodas import virar_direita, motores_parar
import time

def rodar():
    virar_direita()
    time.sleep(2)
    motores_parar()
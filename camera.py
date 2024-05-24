from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()

def tirar_foto(file_path='/home/pi/image.jpg'):
    picam2.start()
    sleep(2)  # Tempo para a câmera ajustar a exposição
    picam2.capture_file(file_path)
    picam2.stop()

def fechar_camera():
    picam2.close()

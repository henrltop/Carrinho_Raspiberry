from picamera import PiCamera
from time import sleep

camera = PiCamera()

def tirar_foto(file_path='/home/pi/image.jpg'):
    camera.start_preview()
    sleep(2)  # Tempo para a câmera ajustar a exposição
    camera.capture(file_path)
    camera.stop_preview()

def fechar_camera():
    camera.close()

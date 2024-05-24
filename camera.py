from picamera2 import Picamera2
from time import sleep
from datetime import datetime

picam2 = Picamera2()

def tirar_foto():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f'/home/pi/image_{timestamp}.jpg'
    picam2.start()
    sleep(2)  # Tempo para a câmera ajustar a exposição
    picam2.capture_file(file_path)
    picam2.stop()
    print(f"Foto salva como {file_path}")

def fechar_camera():
    picam2.close()

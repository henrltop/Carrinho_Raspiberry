from picamera2 import Picamera2, MjpegEncoder
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

def iniciar_gravacao():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f'/home/pi/video_{timestamp}.h264'
    picam2.start()
    picam2.start_recording(MjpegEncoder(), file_path)
    print(f"Gravação iniciada: {file_path}")
    return file_path

def parar_gravacao():
    picam2.stop_recording()
    picam2.stop()
    print("Gravação parada")

def fechar_camera():
    picam2.close()

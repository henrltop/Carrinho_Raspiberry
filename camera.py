from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from time import sleep
from datetime import datetime
import os

picam2 = Picamera2()

def criar_diretorio_se_nao_existir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def tirar_foto():
    diretorio = '/home/fab/Imagens'
    criar_diretorio_se_nao_existir(diretorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(diretorio, f'image_{timestamp}.jpg')
    picam2.start_preview(Preview.NULL)
    picam2.capture_file(file_path)
    picam2.stop_preview()
    print(f"Foto salva como {file_path}")

def iniciar_gravacao():
    diretorio = '/home/fab/Vídeos'
    criar_diretorio_se_nao_existir(diretorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(diretorio, f'video_{timestamp}.h264')
    encoder = H264Encoder()
    output = FileOutput(file_path)
    picam2.start()
    picam2.start_recording(encoder, output)
    print(f"Gravação iniciada: {file_path}")
    return file_path

def parar_gravacao():
    picam2.stop_recording()
    picam2.stop()
    print("Gravação parada")

def fechar_camera():
    picam2.close()
    print("Câmera fechada")

from picamera2 import Picamera2, Preview
from picamera2.outputs import FileOutput
import os
from datetime import datetime

def criar_diretorio_se_nao_existir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

picam2 = Picamera2()

def tirar_foto():
    criar_diretorio_se_nao_existir('/home/fab/Imagens')
    nome_arquivo = '/home/fab/Imagens/foto_{}.jpg'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    picam2.start_preview(Preview.NULL)
    picam2.capture_file(nome_arquivo)
    print(f"Foto salva em: {nome_arquivo}")

def iniciar_gravacao():
    criar_diretorio_se_nao_existir('/home/fab/Vídeos')
    nome_arquivo = '/home/fab/Vídeos/video_{}.h264'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    output = FileOutput(nome_arquivo)
    picam2.start_recording(output)
    print(f"Iniciando gravação... Arquivo: {nome_arquivo}")
    return nome_arquivo

def parar_gravacao():
    picam2.stop_recording()
    print("Gravação parada.")

def fechar_camera():
    picam2.close()
    print("Câmera fechada.")

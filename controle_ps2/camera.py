import cv2
from datetime import datetime
import os

# Função para criar diretório se não existir
def criar_diretorio_se_nao_existir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

# Função para tirar uma foto
def tirar_foto():
    diretorio = '/home/fab/Imagens'
    criar_diretorio_se_nao_existir(diretorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(diretorio, f'image_{timestamp}.jpg')

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(file_path, frame)
        print(f"Foto salva como {file_path}")
    cap.release()

# Função para iniciar gravação de vídeo
def iniciar_gravacao():
    diretorio = '/home/fab/Vídeos'
    criar_diretorio_se_nao_existir(diretorio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(diretorio, f'video_{timestamp}.mp4')

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para mp4
    out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

    print(f"Gravação iniciada: {file_path}")
    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Use 'q' para parar a gravação
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Gravação parada")

# Função para parar a gravação
def parar_gravacao():
    # Esta função não é necessária pois a gravação já é parada com 'q' na função iniciar_gravacao
    pass

# Função para fechar a câmera
def fechar_camera():
    # Esta função não é necessária com o OpenCV, pois a câmera é liberada diretamente nas funções
    pass

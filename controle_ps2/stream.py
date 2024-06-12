import cv2
import subprocess

def iniciar_streaming():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        return

    # Reduzir a resolução e a taxa de quadros para melhorar o desempenho
    width = 320
    height = 240
    fps = 15

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)

    # Comando ffmpeg para transmitir vídeo
    command = [
        'ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', f'{width}x{height}',
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-b:v', '800k',
        '-bufsize', '800k',
        '-f', 'flv',
        '-flvflags', 'no_duration_filesize',  # Adiciona a flag para ignorar a duração e o tamanho do arquivo
        'rtmp://192.168.115.148/live/stream'
    ]

    try:
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        print(f"Erro ao iniciar o subprocesso ffmpeg: {e}")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Erro ao ler o frame")
            break

        try:
            proc.stdin.write(frame.tobytes())
        except Exception as e:
            print(f"Erro ao enviar frame para ffmpeg: {e}")
            break

    cap.release()
    proc.stdin.close()
    proc.wait()

    # Exibir mensagens de erro do FFmpeg
    for line in proc.stderr:
        print(line)

if __name__ == "__main__":
    iniciar_streaming()
    
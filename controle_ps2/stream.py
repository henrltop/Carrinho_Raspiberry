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
        'rtmp://192.168.115.148/live/stream'
    ]

    proc = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Erro ao ler o frame")
            break
        proc.stdin.write(frame.tobytes())

    cap.release()
    proc.stdin.close()
    proc.wait()

if __name__ == "__main__":
    iniciar_streaming()

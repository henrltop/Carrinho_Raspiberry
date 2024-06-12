import cv2
import subprocess

def iniciar_streaming():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao abrir a câmera")
        return

    command = [
        'ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', '640x480',
        '-r', '20',
        '-i', '-',
        '-c:v', 'libx264',
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

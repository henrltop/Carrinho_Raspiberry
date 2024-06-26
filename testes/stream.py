from flask import Flask, Response
import cv2
import subprocess
import numpy as np

app = Flask(__name__)

def capture_screen():
    command = ["ffmpeg", "-f", "x11grab", "-s", "1920x1080", "-i", ":0.0", "-vcodec", "rawvideo", "-pix_fmt", "bgr24", "-an", "-sn", "-f", "rawvideo", "-"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)

    while True:
        raw_frame = process.stdout.read(1920 * 1080 * 3)
        if len(raw_frame) != 1920 * 1080 * 3:
            break
        frame = np.frombuffer(raw_frame, dtype=np.uint8).reshape((1080, 1920, 3))
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(capture_screen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "Stream is running. Navigate to /video_feed to see the stream."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

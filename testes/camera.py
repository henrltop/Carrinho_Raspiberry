from flask import Flask, Response
import cv2
import subprocess
import numpy as np
from threading import Thread

app = Flask(__name__)

def capture_screen():
    command = [
        "ffmpeg", "-f", "x11grab", "-r", "15", "-s", "1280x720", "-i", ":0.0",
        "-vcodec", "rawvideo", "-pix_fmt", "bgr24", "-an", "-sn", "-f", "rawvideo", "-"
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**8)

    while True:
        raw_frame = process.stdout.read(1280 * 720 * 3)
        if len(raw_frame) != 1280 * 720 * 3:
            break
        frame = np.frombuffer(raw_frame, dtype=np.uint8).reshape((720, 1280, 3))
        _, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    camera.release()

@app.route('/screen_feed')
def screen_feed():
    return Response(capture_screen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_feed')
def camera_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '''<h1>Stream is running</h1>
              <p>Navigate to <a href="/screen_feed">Screen Feed</a> to see the screen stream.</p>
              <p>Navigate to <a href="/camera_feed">Camera Feed</a> to see the camera stream.</p>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

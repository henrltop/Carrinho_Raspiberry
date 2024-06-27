from flask import Flask, Response
import subprocess
import numpy as np
from camera import show_camera


show_camera()



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

@app.route('/screen_feed')
def screen_feed():
    return Response(capture_screen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "Stream is running. Navigate to /screen_feed to see the screen stream."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

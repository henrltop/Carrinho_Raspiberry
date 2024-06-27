import cv2

def show_camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_camera()

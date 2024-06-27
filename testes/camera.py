import cv2

def open_camera():
    cap = cv2.VideoCapture(2)
    
    # Definir a resolução para 720p
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Definir a taxa de quadros para 30 fps
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    # Verificar configurações
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Resolução: {width}x{height}, FPS: {fps}")
    
    if not cap.isOpened():
        print("Cannot open camera")
        return
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()

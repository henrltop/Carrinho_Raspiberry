import cv2

def open_camera():
    cap = cv2.VideoCapture(2)  # Use a nova câmera conectada
    
    # Ajuste incremental de resolução e taxa de quadros
    for width, height in [(1280, 720), (640, 480)]:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(f"Tentando resolução: {width}x{height}, Configurada: {actual_width}x{actual_height}")
        
        if actual_width == width and actual_height == height:
            break
    
    cap.set(cv2.CAP_PROP_FPS, 30)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"FPS configurado: {actual_fps}")
    
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

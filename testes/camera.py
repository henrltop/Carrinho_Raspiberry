import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a câmera")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erro ao ler o frame")
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

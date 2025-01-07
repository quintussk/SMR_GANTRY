import cv2

print("Probeer camera te openen...")
camera = cv2.VideoCapture(0)  # Gebruik index 0 voor de standaard camera

if not camera.isOpened():
    print("Kan de camera niet openen. Probeer een andere index.")
else:
    print("Camera geopend! Toon live feed...")
    while True:
        success, frame = camera.read()
        if not success:
            print("Kon geen frame lezen.")
            break
        
        cv2.imshow("Camera Test", frame)  # Toon de camera-output
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Druk 'q' om te stoppen
            break

camera.release()
cv2.destroyAllWindows()
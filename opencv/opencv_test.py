import cv2

camera = cv2.VideoCapture(0)
camera.set(3, 320)         # width (max for c170: 640)
camera.set(4, 240)         # height (max for c170: 480)

while True:
    # read from the camera
    grabbed, frame = camera.read()

    # do some image processing

    # show on the windows
    cv2.imshow('Webcam Streaming', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

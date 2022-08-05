import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    # read from the camera
    _, frame1 = camera.read()
    _, frame2 = camera.read()

    # resize the image
    frame1 = cv2.resize(frame1, (200, 150))
    frame2 = cv2.resize(frame2, (200, 150))

    #flip the frame2
    frame2 = cv2.flip(frame2, 1)

    #using numpy to combine 2 video
    frame = np.hstack((frame1, frame2))


    # show on the windows
    cv2.imshow('Copy and Flip', frame)

    #press q to escape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
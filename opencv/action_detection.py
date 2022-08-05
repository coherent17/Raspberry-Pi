import cv2

camera = cv2.VideoCapture(0)

#set the size of the camera
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


firstFrame = None
skipFrame = 0

while True:
    print("Here")
    _, frame = camera.read()
    text = "Unoccupied"

    #transfer rgb color space to gray color space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #preprocessing the frame -> to reduce the noise and make the frame more smooth
    kernal_size = 21
    gray = cv2.GaussianBlur(gray, (kernal_size, kernal_size), cv2.BORDER_CONSTANT)

    if firstFrame is None:

        #if skip too many frame -> assign default frame
        if skipFrame > 100:
            firstFrame = gray

        text = "Waiting"

        #add text on the original(unpreprocessed frame)
        #usage: cv2.putText(video, text, coordinate, font, fontsize, color, linewidth)
        blue = (0, 0, 255)
        cv2.putText(frame, "Room Status : " + text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, blue, 2)
        cv2.imshow("test1", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        skipFrame += 1
        continue


    print("I am here")
    frameDelta = cv2.absdiff(firstFrame, gray)

    # gray value > thresh -> 255, gray value < thresh -> 0
    # usage : (T, threshImage) = cv2.threshold(src, thresh, maxval, type)
    thresh = 25
    _, thresholded_image = cv2.threshold(frameDelta, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresholded image", thresholded_image)

    # image dilation : combine 2 close but separate objects
    thresholded_image = cv2.dilate(thresholded_image, None, iterations=2)


    # find the contours of the object, only external contour
    # contours is a list, each element represents a contour of the frame
    contours, _ = cv2.findContours(thresholded_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        #if the contourArea is too small, don't draw the contour
        if cv2.contourArea(c) < 500:
            continue

        #draw the bounding box of the contour with red box
        (x, y, w, h) = cv2.boundingRect(c)

        # usage of cv2.rectangle:
        # cv2.rectangle(img, left corner, oppsite corner, color, linewidth)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"


    cv2.putText(frame, "Room Status : " + text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, blue, 2)

    cv2.imshow('test1', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

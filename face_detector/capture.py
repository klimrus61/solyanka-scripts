import cv2
import time 


first_frame = None
video = cv2.VideoCapture(0) # capture computer cam 

while True:

    check, frame = video.read() # first frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # create backgrund image for base
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray) # Отличие между основной кортингой и картинкой в данном фрейме
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # Если цвет пикселя отличается на ... то заменяет его на белый
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) # Контур

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Capturing', gray) # show frame
    cv2.imshow('delta_img', delta_frame)
    cv2.imshow('freshold frame', thresh_frame)
    cv2.imshow('Color frame', frame)


    key = cv2.waitKey(100)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
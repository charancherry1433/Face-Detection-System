# firstly install opecv-python
# we are using haarcascade_frontalface_default.xml, we include it into same directory

# imports right here
import cv2


# for extracting details from cascade classifier
cascadeFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


while True:
    ret, image = cap.read()
    gi = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    f = cascadeFace.detectMultiScale(gi, 1.3, 5)
    
    for (x, y, w, h) in f:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4)
    
    cv2.imshow('image', image)
    k = cv2.waitkey(30) & 0xff
    if k == 27:
        break

cap.release()
cap.destroyAllWindows()
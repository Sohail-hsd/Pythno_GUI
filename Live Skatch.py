import cv2 as cv
import numpy as np

def sketch(image):
    img_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    img_gray_blue = cv.GaussianBlur(img_gray,(5,5),0)
    # canny_edges = cv.Canny(img_gray_blue,50,150)
    canny_edges = cv.Canny(img_gray,10,70)
    ret, mask = cv.threshold(canny_edges, 70, 255, cv.THRESH_BINARY_INV)
    return mask
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('Our live Skatch', sketch(frame))
    if cv.waitKey(1) == 13:
        break
cap.release()
cap.destroyAllWindows()
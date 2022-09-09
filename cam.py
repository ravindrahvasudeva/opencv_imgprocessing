import cv2 as c
import matplotlib.pyplot as mx

cap=c.VideoCapture(0)
ret,frame=cap.read()
mx.imshow(frame)
mx.title("image captured")
mx.show()
cap.release()
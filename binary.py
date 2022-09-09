import cv2
img=cv2.imread("student.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)#if <=150 black
cv2.imshow("student",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
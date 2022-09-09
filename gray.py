import cv2

gray=cv2.imread("student.jpg",0)
cv2.imshow("grayimg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(gray.ndim)
"""
img=cv2.imread("student.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimg",gray)
cv2.waitKey(10000)
cv2.destroyAllWindows()"""
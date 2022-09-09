import cv2 
img=cv2.imread("student.jpg")
cv2.imshow("student",img)
cv2.waitKey(0)                         #to read an image
cv2.destroyAllWindows()
img=cv2.imread("student.jpg")
print(img.ndim)

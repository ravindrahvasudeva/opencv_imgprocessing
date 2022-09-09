import cv2
img=cv2.imread("student.jpg")
height=img.shape[0]
width=img.shape[1]
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),90,2)#wh in tuple,90 is rotation,o.5 is scaling
rotation=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow("image Rotation",rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()

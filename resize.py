import cv2
img=cv2.imread("student.jpg")
#resize=cv2.resize(img,(300,300))                                                   #w,h
resize=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("resize",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
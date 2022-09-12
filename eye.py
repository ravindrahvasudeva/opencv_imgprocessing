import cv2 as c
cascade=c.CascadeClassifier("haarcascade_eye.xml")
img=c.imread("t.webp")
gray=c.cvtColor(img,c.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray,1.2,25)#
for x ,y ,w ,h in faces:
    img=c.rectangle(img,(x,y),(x+w,y+h), (255,0,0),2)
c.imshow("eye detectionnnnnn",img)
c.waitKey(0)
c.destroyAllWindows()
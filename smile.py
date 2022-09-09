import cv2 as c
cascade=c.CascadeClassifier("haarcascade_smile.xml")
img=c.imread("pss.jpg")
gray=c.cvtColor(img,c.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray,1.6,20)#
for x ,y ,w ,h in faces:
    img=c.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
c.imshow("face detectionnnnnn",img)
c.waitKey(0)
c.destroyAllWindows()
import cv2 
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame =cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray,1.06,20)
    for x ,y ,w ,h in faces:
        roi_gray = gray[y:y+h,x:x+w]
        roi_img =frame[y:y+h,x:x+w]
        eye=eye_cascade.detectMultiScale(roi_gray,1.03,6)
        for ex,ey,ew,eh in eye:
         cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
    cv2.imshow("eye detection from video",frame)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
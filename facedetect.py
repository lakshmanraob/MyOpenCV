import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

test = face_cascade.load('/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
eyetest = eye_cascade.load('/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_eye.xml')
print test
print eyetest

img  = cv2.imread('sachin_group.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for (x,y,w,h) in faces:
   img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   roi_gray = gray[y:y+h,x:x+w]
   roi_color = img[y:y+h,x:x+w]
   eyes = eye_cascade.detectMultiScale(roi_gray)
   for (ex,ey,ew,eh) in eyes:
     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

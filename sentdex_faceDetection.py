import cv2
import numpy as np
import picamera

import io

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.capture(stream,format='jpeg')

buff = np.fromstring(stream.getvalue(),dtype=np.uint8)

image = cv2.imdecode(buff,1)

face_cascade = cv2.CascadeClassifier('faces.xml')
print face_cascade

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found "+str(len(faces))+" face(s)"

#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#Save the result image
cv2.imwrite('result.jpg',image)


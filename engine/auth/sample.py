import cv2 as cv

cam=cv.VideoCapture(0, cv.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 400)

detector=cv.CascadeClassifier("engine\\auth\\haarcascade_frontalface_default.xml")

face_id=input("Enter a numeric user ID here...")

print("Collecting samples, look at camera...")

count=0
while True:
  ret, img=cam.read()
  gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  faces_rect=detector.detectMultiScale(gray_img, 1.3, 5)

  for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    count+=1

    cv.imwrite("engine\\auth\\samples\\face."+str(face_id)+"."+str(count)+".jpg", gray_img[y:y+h, x:x+w])
    cv.imshow("Image", img)

  k=cv.waitKey(100) & 0xFF
  if k==27: # Esc key
    break
  elif count>=100:
    break

print("Samples collected successfully...")
cam.release()
cv.destroyAllWindows()
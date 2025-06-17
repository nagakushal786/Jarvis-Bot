from sys import flags
import time
import cv2 as cv
import pyautogui as pg

def face_authentication():
  flag=""

  recognizer=cv.face.LBPHFaceRecognizer_create()
  recognizer.read("engine\\auth\\trainer\\trainer.yml")

  detector=cv.CascadeClassifier("engine\\auth\\haarcascade_frontalface_default.xml")

  font=cv.FONT_HERSHEY_SIMPLEX
  id=2
  names=["", "Kushal"]

  cam=cv.VideoCapture(0, cv.CAP_DSHOW)
  cam.set(3, 640)
  cam.set(4, 480)

  min_w=0.1*cam.get(3)
  min_h=0.1*cam.get(4)

  while True:
    ret, img=cam.read()
    gray_img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces=detector.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5, minSize=(int(min_w), int(min_h)))

    for (x, y, w, h) in faces:
      cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

      id, confidence=recognizer.predict(gray_img[y:y+h, x:x+w])

      if confidence<100:
        id=names[id]
        confidence=" {0}%".format(round(100-confidence))
        flag=1
      else:
        id="unknown"
        confidence=" {0}%".format(round(100-confidence))
        flag=0

      cv.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
      cv.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

    cv.imshow("Camera", img)

    k=cv.waitKey(100) & 0xFF
    if k==27:
      break
    if flag==1:
      break

  cam.release()
  cv.destroyAllWindows()
  return flag
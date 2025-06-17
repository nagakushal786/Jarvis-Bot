import cv2 as cv
import numpy as np
from PIL import Image
import os

path="engine\\auth\\samples"

recognizer=cv.face.LBPHFaceRecognizer_create()
detector=cv.CascadeClassifier("engine\\auth\\haarcascade_frontalface_default.xml")

def train_model(path):
  image_paths=[os.path.join(path, f) for f in os.listdir(path)]
  face_samples=[]
  ids=[]

  for img_path in image_paths:
    gray_img=Image.open(img_path).convert("L")
    img_arr=np.array(gray_img, 'uint8')

    id=int(os.path.split(img_path)[-1].split(".")[1])
    faces=detector.detectMultiScale(img_arr)

    for (x, y, w, h) in faces:
      face_samples.append(img_arr[y:y+h, x:x+w])
      ids.append(id)

  return face_samples, ids

print("Please wait, training the samples...")

faces, ids=train_model(path)
recognizer.train(faces, np.array(ids))

recognizer.write("engine\\auth\\trainer\\trainer.yml")

print("Model trained successfully...")
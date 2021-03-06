import os
import numpy as np
import cv2
from PIL import Image
import pickle

# face_cascade = cv2.CascadeClassifier("src/cascades/data/haarcascade_frontalface_alt2.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "ugo")

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label, path)

            if label not in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            # print(label_ids)

            pil_image = Image.open(path).convert("L")  # grayscale
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            # print(image_array)

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5,
                                                  minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                # print(x, y, w, h)
                roi = image_array[y:y + h, x:x + w]
                x_train.append(roi)
                y_labels.append(id_)

# print(x_train)
# print(y_labels)

with open("labels.pkl", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")

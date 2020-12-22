import face_recognition as fr
import numpy as np
import cv2
import os

def encode_image(path):
    img = fr.load_image_file(f"images/{path}")
    return fr.face_encodings(img)[0]

encodings = np.array(list(map(encode_image, os.listdir('images/'))))
image = fr.load_image_file("images/muskan.png")
image = fr.face_encodings(image)[0]
print(fr.compare_faces(encodings, image))
print(fr.face_distance(encodings, image))


# img = fr.load_image_file('images/shreya.jpeg')
# locations = fr.face_locations(img)
# locations = locations[0]
#
# img = cv2.rectangle(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), (locations[1], locations[0]), (locations[3], locations[2]), (0,255,0), 2)
# cv2.imshow("shreya", img)

import face_recognition as fr
import numpy as np
import cv2
import os
import sys

from reader import reading_encodings

IMAGES_LIST = os.listdir(f'images/{sys.argv[1]}/')
encodings = reading_encodings(sys.argv[1])['encodings']
#encodings = np.array(list(map(encode_image, IMAGES_LIST)))
# image = fr.load_image_file("images/muskan.png")
# image = fr.face_encodings(image)[0]
# print(fr.compare_faces(encodings, image))
# print(fr.face_distance(encodings, image))

webcam = cv2.VideoCapture(0)
if not webcam.read(0)[0]:
    webcam = cv2.VideoCapture(1)

recognised = []

while(recognised==[]):
    for i in range(10):
        status, frame = webcam.read()

        try:
            locations = fr.face_locations(frame)
            locations = locations[0]

            image = fr.face_encodings(frame)[0]
            matches = fr.face_distance(encodings, image)
            i = np.where(matches==min(matches))[0][0]
            name = IMAGES_LIST[i].split('.')[0]
            recognised.append(name)

        except:
            locations = (0,0,0,0)
            name =''

        frame = cv2.rectangle(frame, (locations[1], locations[0]), (locations[3], locations[2]), (0,255,0), 2)
        frame = cv2.putText(frame, name,  (locations[3], locations[2]+20), cv2.FONT_HERSHEY_SIMPLEX ,  1, (0,255,0), 2, cv2.LINE_AA)

        cv2.imshow("webcam", frame)
        cv2.waitKey(20)

print(recognised)
person = max(recognised, key = recognised.count)
print(person)


# img = fr.load_image_file('images/shreya.jpeg')
# locations = fr.face_locations(img)
# locations = locations[0]
#
# img = cv2.rectangle(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), (locations[1], locations[0]), (locations[3], locations[2]), (0,255,0), 2)
# cv2.imshow("shreya", img)

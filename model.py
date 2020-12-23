import face_recognition as fr
import numpy as np
import cv2
import os

IMAGES_LIST = os.listdir('images/')

def encode_image(path):
    img = fr.load_image_file(f"images/{path}")
    return fr.face_encodings(img)[0]

encodings = np.array(list(map(encode_image, IMAGES_LIST)))
# image = fr.load_image_file("images/muskan.png")
# image = fr.face_encodings(image)[0]
# print(fr.compare_faces(encodings, image))
# print(fr.face_distance(encodings, image))

webcam = cv2.VideoCapture(0)
if not webcam.read(0)[1]:
    webcam = cv2.VideoCapture(1)

while(True):
    status, frame = webcam.read()

    locations = fr.face_locations(frame)
    locations = locations[0]

    image = fr.face_encodings(frame)[0]
    matches = fr.face_distance(encodings, image)
    i = np.where(matches==min(matches))[0][0]
    name = IMAGES_LIST[i].split('.')[0]

    frame = cv2.rectangle(frame, (locations[1], locations[0]), (locations[3], locations[2]), (0,255,0), 2)
    frame = cv2.putText(frame, name,  (locations[3], locations[2]+20), cv2.FONT_HERSHEY_SIMPLEX ,  1, (0,255,0), 2, cv2.LINE_AA)

    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# img = fr.load_image_file('images/shreya.jpeg')
# locations = fr.face_locations(img)
# locations = locations[0]
#
# img = cv2.rectangle(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), (locations[1], locations[0]), (locations[3], locations[2]), (0,255,0), 2)
# cv2.imshow("shreya", img)

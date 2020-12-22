import face_recognition as fr
import cv2

img = fr.load_image_file('images/shreya.jpeg')
locations = fr.face_locations(img)
locations = locations[0]

img = cv2.rectangle(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), (locations[1], locations[0]), (locations[3], locations[2]), (0,255,0), 2)
cv2.imshow("shreya", img)
cv2.waitKey(0)

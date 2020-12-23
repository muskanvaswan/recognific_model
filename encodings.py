import os
import numpy as np
import face_recognition as fr
import pickle


IMAGES_LIST = os.listdir('images/')

def encode_image(path):
    img = fr.load_image_file(f"images/{path}")
    try:
        return fr.face_encodings(img)[0]
    except:
        pass

encodings = np.array(list(map(encode_image, IMAGES_LIST)))
encodings = { "encodings": encodings}

# opening file in write mode (binary)
file = open("encodings/encoded.txt", "wb")

# serializing dictionary
pickle.dump(encodings, file)
# closing the file
file.close()

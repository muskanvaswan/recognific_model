import os
import numpy as np
import face_recognition as fr
import pickle
import sys

IMAGES_LIST = os.listdir(f'images/{sys.argv[1]}/')

def encode_image(path):
    img = fr.load_image_file(f"images/{sys.argv[1]}/{path}")
    try:
        return fr.face_encodings(img)[0]
    except:
        pass

encodings = np.array(list(map(encode_image, IMAGES_LIST)))
encodings = { "encodings": encodings}

# opening file in write mode (binary)
file = open(f"encodings/{sys.argv[1]}.txt", "wb+")

# serializing dictionary
pickle.dump(encodings, file)
# closing the file
file.close()

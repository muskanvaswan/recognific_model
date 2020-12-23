import pickle


def reading_encodings():
    # reading the data from the file
    with open('encodings/encoded.txt', 'rb') as handle:
        data = handle.read()
    # reconstructing the data as dictionary
    d = pickle.loads(data)
    return d

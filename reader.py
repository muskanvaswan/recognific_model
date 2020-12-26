import pickle


def reading_encodings(path):
    # reading the data from the file
    with open(f'encodings/{path}.txt', 'rb') as handle:
        data = handle.read()
    # reconstructing the data as dictionary
    d = pickle.loads(data)
    return d

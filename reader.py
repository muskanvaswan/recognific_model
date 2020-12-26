import pickle
import csv

def reading_encodings(path):
    # reading the data from the file
    with open(f'encodings/{path}.txt', 'rb') as handle:
        data = handle.read()
    # reconstructing the data as dictionary
    d = pickle.loads(data)
    return d

def csv_writter(ls):
    with open('Attendance/sample.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ls)

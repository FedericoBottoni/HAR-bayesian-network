import pandas as pd
import csv
from random import shuffle
from pgmNetwork import pgmNetwork
from Config import Config

def dsShuffle():
    print('LOG: Shuffling the dataset')
    data=list()

    with open('data/Dataset.csv', mode='r', newline="\r\n", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n')
        for row in csv_reader:
                data.append(row)

    header=data[:2]
    data=data[2:]
    shuffle(data)
    data=header+data

    with open('data/Shuffled.csv', mode='w+', newline="\n", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row) 

    print('LOG: Parsing data')
    # parse data according to the library
    parsedData = []

    print('LOG: Discretizing the dataset')
    config = Config()
    # discretize data using range

    pgmNetwork(parsedData)
    
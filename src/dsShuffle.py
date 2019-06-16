import pandas as pd
import csv
from random import shuffle
from pgmNetwork import pgmNetwork
from Snapshot import Snapshot
from Config import Config

def dsShuffle():
    print('LOG: Shuffling the dataset')
    data=list()

    with open('data/FixedDataset.csv', mode='r', newline="\r\n", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n')
        firstLine = True
        for row in csv_reader:
            if not firstLine:
                data.append(row)
            else:
                head = row
                firstLine = False

    shuffle(data)

    #with open('data/Shuffled.csv', mode='w+', newline="\n", encoding="utf-8") as csv_file:
    #    csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
    #    csv_writer.writerow(head) 
    #    for row in data:
    #        csv_writer.writerow(row) 

    print('LOG: Parsing data')
    snapshots = list()
    for row in data:
        snapshots.append(Snapshot(row))

    parsedData = list()
    test = list()
    print('LOG: Discretizing the dataset')
    config = Config()
    line = 0
    for row in snapshots:
        line += 1
        if line <= len(snapshots) * 0.75:
            parsedData.append(row.getDiscretizedInstance(config.getRangeSize()))
        else:
            test.append(row.getDiscretizedInstance(config.getRangeSize()))

    pgmNetwork(parsedData, test)
    
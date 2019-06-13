import libpgm as lp
import pandas as pd
import csv
from random import shuffle

data=list()

with open('Dataset.csv', mode='r', newline="\r\n", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n')
    for row in csv_reader:
            data.append(row)

header=data[:2]
data=data[2:]
shuffle(data)
data=header+data

with open('Shuffled.csv', mode='w+', newline="\n", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        csv_writer.writerow(row)
import pandas as pd
import csv
from random import shuffle
from process import normalizeDataset, encodeClass
from pgmNetwork import testModel, generateCpds, generateSkeleton
from Snapshot import Snapshot
from Config import Config

def dsShuffle(mod):
    config = Config()

    print('LOG: Preprocessing data')
    data=list()
    with open('data/FixedDataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        data = normalizeDataset(csv_reader)
    shuffle(data)

    #with open('data/Shuffled.csv', mode='w+', newline="\n", encoding="utf-8") as csv_file:
    #    csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
    #    csv_writer.writerow(head) 
    #    for row in data:
    #        csv_writer.writerow(row) 
    
    snapshots = list()
    line = 0
    for row in data:
        if line < len(data) * config.percGetData():
            snapshots.append(Snapshot(row))
        line += 1

    if mod == 'skeleton':
        generateSkeleton(snapshots)
    elif mod == 'cpds':
        generateCpds(snapshots)
    elif mod == 'test':
        testModel(snapshots)

def makeInference(query):
    raise Exception('Not implemented: parse the query and call testModel with a single snapshot')

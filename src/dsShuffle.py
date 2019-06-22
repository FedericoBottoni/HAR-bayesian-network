import pandas as pd
import csv
from py_linq import Enumerable
from process import normalizeDataset, encodeClass, featuresMean, featuresStd
import pgmNetwork
import pomegranateNetwork
from Snapshot import Snapshot
from Config import Config

def dsShuffle(mod):
    config = Config()

    print('LOG: Preprocessing data')
    data = getData()
    with open('data/FixedDataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        data_mean = featuresMean(csv_reader)
    with open('datasetMeasures/FeaturesMean.txt', 'w+') as file:
        file.write(str(data_mean))
    with open('data/FixedDataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        data_std = featuresStd(csv_reader)
    with open('datasetMeasures/FeaturesStd.txt', 'w+') as file:
        file.write(str(data_std))
    #with open('data/Shuffled.csv', mode='w+', newline="\n", encoding="utf-8") as csv_file:
    #    csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', lineterminator='\r\n', quoting=csv.QUOTE_MINIMAL)
    #    csv_writer.writerow(head) 
    #    for row in data:
    #        csv_writer.writerow(row) 
    
    snapshots = list()
    tests = list()
    line = 0
    for row in data:
        if line < len(data) * config.percGetData():
            snapshots.append(Snapshot(row))
        else:
            tests.append(Snapshot(row))
        line += 1

    if mod == 'skeleton':
        pomegranateNetwork.generateSkeleton(snapshots)
    elif mod == 'cpds':
        #pomegranateNetwork.generateCpds(snapshots)
        pass
    elif mod == 'test':
        pomegranateNetwork.testModel(snapshots, tests)

def getData():
    data=list()
    with open('data/FixedDataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        data = normalizeDataset(csv_reader)
    return data

def makeInference(query):
    config = Config()
    attCouples = Enumerable(query.split(';')).select(lambda x: x.split('=')).to_list()
    row = Enumerable(config.evidences()).select(lambda x: getVals(x, attCouples)).to_list()
    row.append(None)
    snap = Snapshot(row)
    print(snap.toString())
    pomegranateNetwork.testModel(snap, getData())

    
def getVals(x, attCouples): 
        values = Enumerable(attCouples).where(lambda y: x == y[0]).to_list()
        if len(values) == 1:
            return values[0][1]
        elif len(values) == 0:
            raise Exception('Missing param: "' + x + '"')
        else:
            raise Exception('Param "' + x + '" given more then one time')
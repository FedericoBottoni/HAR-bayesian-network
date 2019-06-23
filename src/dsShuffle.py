import pandas as pd
import csv
import json
from py_linq import Enumerable
from process import preProcess
import pomegranateNetwork
from random import shuffle
from Snapshot import Snapshot
from Config import Config

def dsShuffle(mod):
    config = Config()
    print('LOG: Preprocessing data')
    data = getData()
    preSnaps = preProcess(data)   
    shuffle(data)
    snapshots = preSnaps[:int(len(data) * config.percGetData())]
    tests = preSnaps[int(len(data) * config.percGetData()):]
    if mod == 'skeleton':
        pomegranateNetwork.generateSkeleton(snapshots)
    elif mod == 'test':
        pomegranateNetwork.testModel(snapshots, tests)

def getData():
    data=list()
    with open('data/FixedDataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for sample in csv_reader:
            data.append(Snapshot([int(sample['x1']), int(sample['y1']), int(sample['z1']), int(sample['x2']), int(sample['y2']), int(sample['z2']), int(sample['x3']), int(sample['y3']), int(sample['z3']), int(sample['x4']), int(sample['y4']), int(sample['z4']), sample['class']]))    
    return data

def makeInference(query):
    config = Config()
    print('LOG: Preprocessing data')
    snapshots = list()
    if query != None:
        snap = [parseInference(query)]
    else:
        print('LOG: Reading queries from "' + config.inInference() + '"')
        with open(config.inInference()) as json_file:  
            data = json.load(json_file)
        snap = Enumerable(data).select(parseInference).to_list()
    snapshots.extend(snap)
    snapshots.extend(getData())
    postSnapshots = preProcess(snapshots)
    pomegranateNetwork.inference(postSnapshots[len(snap):], postSnapshots[:len(snap)])

def parseInference(query):
    config = Config()
    attCouples = Enumerable(query.split(';')).select(lambda x: x.split('=')).to_list()
    row = Enumerable(config.evidences()).select(lambda x: getVals(x, attCouples)).to_list()
    row.append(None)
    return Snapshot(row)
    
def getVals(x, attCouples): 
        values = Enumerable(attCouples).where(lambda y: x == y[0]).to_list()
        if len(values) == 1:
            return values[0][1]
        elif len(values) == 0:
            raise Exception('Missing param: "' + x + '"')
        else:
            raise Exception('Param "' + x + '" given more then one time')
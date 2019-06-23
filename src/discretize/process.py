from sklearn.preprocessing import normalize
from sklearn.preprocessing import KBinsDiscretizer
from random import shuffle
from Config import Config

import numpy as np

def normalizeDataset(csv_reader):
    config = Config()
    data = np.empty([165633,13])
    i = 0
    for sample in csv_reader:
        data[i, 0] = sample['x1']
        data[i, 1] = sample['y1']
        data[i, 2] = sample['z1']
        data[i, 3] = sample['x2']
        data[i, 4] = sample['y2']
        data[i, 5] = sample['z2']
        data[i, 6] = sample['x3']
        data[i, 7] = sample['y3']
        data[i, 8] = sample['z3']
        data[i, 9] = sample['x4']
        data[i, 10] = sample['y4']
        data[i, 11] = sample['z4']
        data[i, 12] = encodeClass(sample['class'])
        i = i + 1
    data=data.tolist()
    shuffle(data)
    #data=data[:int(len(data)*0.1)]
    data=np.array(data)
    #indaga su axis: sulla doc dicono che 0 normalizza per features su so dicono che sia 1....
    data_tmp = normalize(data[:, np.arange(12)], norm = 'l2', axis = 0, return_norm = False)
    est = KBinsDiscretizer(n_bins = config.nOfBuckets(), encode='ordinal').fit(data_tmp)
    data_discretize = est.transform(data_tmp)
    data = np.concatenate((data_discretize, data[:, [12]]), axis = 1)
    #Ora è data a contenere tutte le colonne discretizzate meno l'ultima, quindi sotto devo modificare.
    return data

def featuresMean(csv_reader):
    config = Config()
    data = np.empty([165633,12])
    i = 0
    for sample in csv_reader:
        data[i, 0] = sample['x1']
        data[i, 1] = sample['y1']
        data[i, 2] = sample['z1']
        data[i, 3] = sample['x2']
        data[i, 4] = sample['y2']
        data[i, 5] = sample['z2']
        data[i, 6] = sample['x3']
        data[i, 7] = sample['y3']
        data[i, 8] = sample['z3']
        data[i, 9] = sample['x4']
        data[i, 10] = sample['y4']
        data[i, 11] = sample['z4']
        i = i + 1
    data_mean = np.mean(data, axis=0)
    return data_mean

def featuresStd(csv_reader):
    config = Config()
    data = np.empty([165633,12])
    i = 0
    for sample in csv_reader:
        data[i, 0] = sample['x1']
        data[i, 1] = sample['y1']
        data[i, 2] = sample['z1']
        data[i, 3] = sample['x2']
        data[i, 4] = sample['y2']
        data[i, 5] = sample['z2']
        data[i, 6] = sample['x3']
        data[i, 7] = sample['y3']
        data[i, 8] = sample['z3']
        data[i, 9] = sample['x4']
        data[i, 10] = sample['y4']
        data[i, 11] = sample['z4']
        i = i + 1
    data_std = np.std(data, axis=0)
    return data_std


def encodeClass(classStr):
    return ['walking', 'standing', 'standingup', 'sitting', 'sittingdown'].index(classStr)

def decodeClass(classStr):
    return ['walking', 'standing', 'standingup', 'sitting', 'sittingdown'][classStr]
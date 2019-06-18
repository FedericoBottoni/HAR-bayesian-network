from sklearn.preprocessing import normalize
import numpy as np

def normalizeDataset(csv_reader):
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
    normalize(data, norm = 'l2', axis = 1, copy = False, return_norm = False)
    return data

def encodeClass(classStr):
    try:
        clss = ['walking', 'standing', 'standingup', 'sitting', 'sittingdown'].index(classStr)
    except:
        clss = -1
    return clss

def decodeClass(classStr):
    try:
        clss = ['walking', 'standing', 'standingup', 'sitting', 'sittingdown'][classStr]
    except:
        clss = ''
    return clss
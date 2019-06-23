from sklearn.preprocessing import normalize
from sklearn.preprocessing import KBinsDiscretizer
from py_linq import Enumerable
from Snapshot import Snapshot
from Config import Config

import numpy as np

def preProcess(snaps):
    config = Config()
    data = np.empty([len(snaps),13])
    i = 0
    for snap in snaps:
        data[i, 0] = snap.x1
        data[i, 1] = snap.y1
        data[i, 2] = snap.z1
        data[i, 3] = snap.x2
        data[i, 4] = snap.y2
        data[i, 5] = snap.z2
        data[i, 6] = snap.x3
        data[i, 7] = snap.y3
        data[i, 8] = snap.z3
        data[i, 9] = snap.x4
        data[i, 10] = snap.y4
        data[i, 11] = snap.z4
        data[i, 12] = encodeClass(snap.harClass)
        i = i + 1
    data=data.tolist()
    data=np.array(data)
    data_tmp = normalize(data[:, np.arange(12)], norm = 'l2', axis = 0, return_norm = False)
    est = KBinsDiscretizer(n_bins = config.nOfBuckets(), encode='ordinal').fit(data_tmp)
    data_discretize = est.transform(data_tmp)
    data = np.concatenate((data_discretize, data[:, [12]]), axis = 1)
    return Enumerable(data).select(lambda x: Snapshot(x)).to_list()

def encodeClass(classStr):
    return None if classStr == None else ['walking', 'standing', 'standingup', 'sitting', 'sittingdown'].index(classStr)

def decodeClass(classStr):
    return None if classStr == None else ['walking', 'standing', 'standingup', 'sitting', 'sittingdown'][classStr]
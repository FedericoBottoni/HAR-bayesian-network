from sklearn.preprocessing import normalize
import numpy as np
import csv

data = np.empty([165633,12])
i = 0
#Change path
with open('FixedDataset.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
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
#print(data)
normalize(data, norm = 'l2', axis = 1, copy = False, return_norm = False)
#print(data)
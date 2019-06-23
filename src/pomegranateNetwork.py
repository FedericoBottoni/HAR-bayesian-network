import pandas as pd
import numpy as np
import json
from py_linq import Enumerable
from process import decodeClass
from Config import Config
#from pytictoc import TicToc
from pomegranate import BayesianNetwork

def getDataFrames(snaps):
    config = Config()
    x1 = list() 
    y1 = list() 
    z1 = list() 
    x2 = list() 
    y2 = list() 
    z2 = list() 
    x3 = list() 
    y3 = list() 
    z3 = list() 
    x4 = list() 
    y4 = list() 
    z4 = list() 
    harClass = list() 
    for row in snaps:
        x1.append(row.x1)
        y1.append(row.y1)
        z1.append(row.z1)
        x2.append(row.x2)
        y2.append(row.y2)
        z2.append(row.z2)
        x3.append(row.x3)
        y3.append(row.y3)
        z3.append(row.z3)
        x4.append(row.x4)
        y4.append(row.y4)
        z4.append(row.z4)
        harClass.append(row.harClass)
    return pd.DataFrame(data={'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2, 'x3':x3, 'y3':y3, 'z3':z3, 'x4':x4, 'y4':y4, 'z4':z4, 'class': harClass})

def parseVal(val):
    try:
        res = decodeClass(int(val))
    except:
        res = 'None'
    return res

def generateSkeleton(data):
    config = Config()
    dfrm = getDataFrames(data)
    print('LOG: Generate Skeleton')
    model = BayesianNetwork.from_samples(dfrm, algorithm='greedy', state_names=config.variables())
    with open('generatedSkeleton/skeletonGraph'+str(config.nOfBuckets())+'buckets.txt', "w+") as f:
        f.write(model.to_json())


def inference(data, infs):
    config = Config()
    dfrm = getDataFrames(data)
    model = BayesianNetwork.from_samples(dfrm, reduce_dataset=True, algorithm='greedy', state_names=config.variables())
    model.bake()
    testsArray = np.array(Enumerable(infs).select(lambda x: [x.x1, x.y1, x.z1, x.x2, x.y2, x.z2, x.x3, x.y3, x.z3, x.x4, x.y4, x.z4, None]).to_list())
    print('LOG: Predicting')
    prediction = model.predict(testsArray)
    if len(infs) > 1:
        print('LOG: Printing predictions in "' + config.outInference() + '"')
        with open(config.outInference(), "w+") as f:
            f.write('\n'.join(Enumerable(prediction).select(lambda x: str(x) + ' ' + parseVal(x[12])).to_list()))
    else:
        print('Predicted value is "' + parseVal(prediction[0][12]) + '"')

def testModel(data, tests):
    dfrm = getDataFrames(data)
    model = BayesianNetwork.from_samples(dfrm, reduce_dataset=True, algorithm='greedy', state_names=config.variables())
    model.bake()
    testsArray = np.array(Enumerable(tests).select(lambda x: [x.x1, x.y1, x.z1, x.x2, x.y2, x.z2, x.x3, x.y3, x.z3, x.x4, x.y4, x.z4, None]).to_list())
    tags = np.array(Enumerable(tests).select(lambda x: x.harClass).to_list())
    print('LOG: Testing')
    prediction = model.predict(testsArray)
    i=0
    corrects=0
    for p in prediction:
        if(p[12]==tags[i]):
            corrects+=1
        i+=1
    print('Score: ' + str(corrects*100/len(tests)) + '%')
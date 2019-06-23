import pandas as pd
import numpy as np
import json
from py_linq import Enumerable
from process import decodeClass
from importCpd import importCpd
from Config import Config
from ConfigBn import ConfigBn
from pytictoc import TicToc
from pomegranate import BayesianNetwork

def generateSkeleton(data):
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
    for row in data:
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
    dfrm = pd.DataFrame(data={'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2, 'x3':x3, 'y3':y3, 'z3':z3, 'x4':x4, 'y4':y4, 'z4':z4, 'class': harClass})
    print('LOG: Generate Skeleton')
    t = TicToc() #create instance of class
    t.tic() #Start timer
    #skel, sep_sets = est.estimate_skeleton()
    model = BayesianNetwork.from_samples(dfrm, algorithm='greedy', state_names=["x1", "y1", "z1","x2", "y2", "z2","x3", "y3", "z3","x4", "y4", "z4","class"])
    t.toc() #Time elapsed since t.tic()
    #print(skel.edges())
    with open('generatedSkeleton/skeletonGraph'+str(config.nOfBuckets())+'buckets.txt', "w+") as f:
        f.write(model.to_json())



def testModel(data, tests):


    bnet = ConfigBn()
    config = Config()
    
    
    #f=open('generatedSkeleton/SkeletonGraph'+str(config.nOfBuckets())+'buckets.txt', "r", newline="\r\n", encoding="utf-8")
    #model=BayesianNetwork.from_json(f.read())
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
    for row in data:
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
    dfrm = pd.DataFrame(data={'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2, 'x3':x3, 'y3':y3, 'z3':z3, 'x4':x4, 'y4':y4, 'z4':z4, 'class': harClass})
    
    model = BayesianNetwork.from_samples(dfrm, reduce_dataset=True, algorithm='greedy', state_names=["x1", "y1", "z1","x2", "y2", "z2","x3", "y3", "z3","x4", "y4", "z4","class"])
    model.bake()
    #t = TicToc() #create instance of class
    #t.tic() #Start timer
    #print(model.score(np.array([[tests[0].x1, tests[0].y1, tests[0].z1, tests[0].x2, tests[0].y2, tests[0].z2, tests[0].x3, tests[0].y3, tests[0].z3, tests[0].x4, tests[0].y4, tests[0].z4, tests[0].harClass],[tests[1].x1, tests[1].y1, tests[1].z1, tests[1].x2, tests[1].y2, tests[1].z2, tests[1].x3, tests[1].y3, tests[1].z3, tests[1].x4, tests[1].y4, tests[1].z4, tests[1].harClass]]), np.array([tests[0].harClass,tests[1].harClass])))
    #a = np.array(Enumerable(tests).select(lambda x: [x.x1, x.y1, x.z1, x.x2, x.y2, x.z2, x.x3, x.y3, x.z3, x.x4, x.y4, x.z4, x.harClass]).to_list())
    #b = np.array(Enumerable(tests).select(lambda x: x.harClass).to_list())
    #print(model.score(a, b))
    #t.toc() #Time elapsed since t.tic()

    testsArray = np.array(Enumerable(tests).select(lambda x: [x.x1, x.y1, x.z1, x.x2, x.y2, x.z2, x.x3, x.y3, x.z3, x.x4, x.y4, x.z4, None]).to_list())
    tags = np.array(Enumerable(tests).select(lambda x: x.harClass).to_list())

    prediction = model.predict(testsArray)
    i=0
    corrects=0
    for p in prediction:
        if(p[12]==tags[i]):
            corrects+=1
    
    print('Score: ' + str(corrects*100/len(tests)) + '%')
    
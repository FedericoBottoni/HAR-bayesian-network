import pandas as pd
import numpy as np
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
    est = ConstraintBasedEstimator(dfrm)
    t = TicToc() #create instance of class
    t.tic() #Start timer
    #skel, sep_sets = est.estimate_skeleton()
    model = BayesianNetwork.from_samples(dfrm, algorithm='greedy')
    t.toc() #Time elapsed since t.tic()
    #print(skel.edges())
    f=open('generatedSkeleton/skeletonGraph'+str(config.nOfBuckets())+'buckets.txt', "w+")
    f.write(str(model.graph))
    f.close()
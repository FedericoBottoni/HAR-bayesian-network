import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, ConstraintBasedEstimator
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from py_linq import Enumerable
from process import decodeClass
from importCpd import importCpd
from Config import Config
from ConfigBn import ConfigBn
from pomegranate import BayesianNetwork

def nextCpd(varName, bnet, config):
    card = config.nOfBuckets() if varName in config.evidences() else 5
    evidences = Enumerable(bnet.getNetwork()).where(lambda x: x[1] == varName).select(lambda x: x[0])
    return TabularCPD(varName, card, importCpd(varName), evidence=list(evidences), evidence_card=list(evidences.select(lambda x: config.nOfBuckets())))

def testModel(tests):


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
    for row in tests:
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
    
    model = BayesianNetwork.from_samples(dfrm, algorithm='greedy', state_names=["x1", "y1", "z1","x2", "y2", "z2","x3", "y3", "z3","x4", "y4", "z4","class"])
    model.bake()
    print(model.probability([[2,3,0,0,0,0,2,3,3,1,3,4,4]]))
    print(model.edge_count())
    print(model.node_count())
    prediction = model.predict([[2,3,0,0,0,0,2,3,3,1,3,4,None]])

    print('LOG: Making the network')
    model = BayesianModel(bnet.getNetwork())
    for varName in config.variables():
        #print(importCpd(varName))
        model.add_cpds(nextCpd(varName, bnet, config))
    print('LOG: Variable Elimination')
    infer = VariableElimination(model)
    if isinstance(tests, list):
        print('LOG: Queries')
        line = 1
        correctEntries = 0
        for test in tests:
            print(str(line) + '- Waited: ' + decodeClass(int(test.harClass)))
            q = infer.query(['class'], evidence={'x1':test.x1, 'y1':test.y1, 'z1':test.z1, 'x2':test.x2, 'y2':test.y2, 'z2':test.z2, 'x3':test.x3, 'y3':test.y3, 'z3':test.z3, 'x4':test.x4, 'y4':test.y4, 'z4':test.z4})
            maxPhi = np.argmax(q.values)
            if maxPhi == test.harClass:
                correctEntries += 1
            print(q.values)
            print(str(line) + '- Got: ' + decodeClass(int(maxPhi))+ '\n')
            line += 1
        print('Model precision: ' + str(correctEntries*100/len(tests)) + '%')
    else:
        q = infer.query(['class'], evidence={'x1':test.x1, 'y1':test.y1, 'z1':test.z1, 'x2':test.x2, 'y2':test.y2, 'z2':test.z2, 'x3':test.x3, 'y3':test.y3, 'z3':test.z3, 'x4':test.x4, 'y4':test.y4, 'z4':test.z4})
        maxPhi = np.argmax(q.values)
        print(maxPhi)

def generateCpds(data):
    bnet = ConfigBn()
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
    print('LOG: Making the network')
    model = BayesianModel(bnet.getNetwork())
    print('LOG: Stimate CPDs')
    dfrm = pd.DataFrame(data={'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2, 'x3':x3, 'y3':y3, 'z3':z3, 'x4':x4, 'y4':y4, 'z4':z4, 'class': harClass})
    for varName in config.variables():
        cpd_C = MaximumLikelihoodEstimator(model, dfrm).estimate_cpd(varName)
        print('LOG: CPD wrote in "generatedCPDs/' + varName + '.txt"')
        f=open('generatedCPDs/' + varName + '.txt', "w+")
        f.write(str(cpd_C.get_values()))
        f.close()


def generateSkeleton(data):
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
    skel, sep_sets = est.estimate_skeleton()
    print(skel.edges())
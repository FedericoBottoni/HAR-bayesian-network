import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator, MaximumLikelihoodEstimator, ConstraintBasedEstimator
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from Config import Config
from ConfigBn import ConfigBn

def testModel(tests):
    config = ConfigBn()
    
    print('LOG: Making the network')
    model = BayesianModel(config.getNetwork())
    cpd_class = TabularCPD('class', 5, config.getCpd()) # Possiblity to add entries evidence=['diff', 'intel'], evidence_card=[2,3])
    print('LOG: Variable Elimination')
    infer = VariableElimination(model)
    if isinstance(query, list):
        print('LOG: Queries')
        correctEntries = 0
        line = 0
        for test in tests:
            line += 1
            if line < 11: 
                print(test.toDiscretizedString(config.getRangeSize()))
                q = infer.query(['class'], evidence={'x1':test.x1, 'y1':test.y1, 'z1':test.z1, 'x2':test.x2, 'y2':test.y2, 'z2':test.z2, 'x3':test.x3, 'y3':test.y3, 'z3':test.z3, 'x4':test.x4, 'y4':test.y4, 'z4':test.z4})
                maxPhi = np.argmax(q.values)
                if maxPhi == test.harClass:
                    correctEntries += 1
                print(q.values)
                print(maxPhi)
        print('Model precision: ' + str(correctEntries*100/len(tests)) + '%')
    else:
        q = infer.query(['class'], evidence={'x1':test.x1, 'y1':test.y1, 'z1':test.z1, 'x2':test.x2, 'y2':test.y2, 'z2':test.z2, 'x3':test.x3, 'y3':test.y3, 'z3':test.z3, 'x4':test.x4, 'y4':test.y4, 'z4':test.z4})
        maxPhi = np.argmax(q.values)
        print(maxPhi)

def generateCpds(data):
    config = ConfigBn()
    
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
    model = BayesianModel(config.getNetwork())
    print('LOG: Stimate CPDs')
    dfrm = pd.DataFrame(data={'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2, 'x3':x3, 'y3':y3, 'z3':z3, 'x4':x4, 'y4':y4, 'z4':z4, 'class': harClass})
    estimator = BayesianEstimator(model, dfrm)
    cpd_C = MaximumLikelihoodEstimator(model, dfrm).estimate_cpd('class')
    print(cpd_C.get_values())
    f=open('lucafoppa.txt', "w+")
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

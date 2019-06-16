import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
#from pgmpy.inference import VariableElimination
from Config import Config

def pgmNetwork(data, test):
    config = Config()
    
    user = list() 
    howTallInMeters = list() 
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
        user.append(row.user)
        howTallInMeters.append(row.howTallInMeters)
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
    print('LOG: Making the estimator')
    dfrm = pd.DataFrame(data={'user':user, 'howTallInMeters':howTallInMeters, 'x1':x1, 'y1':y1, 'z1':z1, 'x2':x2, 'y2':y2, 'z2':z2, 'x3':x3, 'y3':y3, 'z3':z3, 'x4':x4, 'y4':y4, 'z4':z4, 'class': harClass})
    estimator = BayesianEstimator(model, dfrm)
    #cpd_C = estimator.estimate_cpd('class', prior_type="K2"  )
    #print(cpd_C)
    #infer = VariableElimination(model)
    #print(infer.query(['harClass'], evidence={}))
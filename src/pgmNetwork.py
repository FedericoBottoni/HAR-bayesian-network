import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
from Config import Config

def pgmNetwork(data):
    config = Config()
    print('LOG: Making the network')
    model = BayesianModel(config.getNetwork())
    #estimator = BayesianEstimator(model, data)
    #cpd_C = estimator.estimate_cpd('C', prior_type="dirichlet", pseudo_counts=[1, 2])
    #print(cpd_C)
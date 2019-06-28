
class Config():

    def percGetData(self):
        return 0.9

    def nOfBuckets(self):
        return 5

    def evidences(self):
        return ['x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3', 'x4', 'y4', 'z4']

    def variables(self):
        vrbls = self.evidences()
        vrbls.extend(['class'])
        return vrbls

    def inInference(self):
        return 'inference/in.txt'
    
    def outInference(self):
        return 'inference/out.txt'
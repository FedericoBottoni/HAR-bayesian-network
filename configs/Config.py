
class Config():

    def percGetData(self):
        return 0.9

    def nOfBuckets(self):
        return 5

    def evidences(self):
        return ['x1', 'x2', 'x3', 'x4', 'y1', 'y2', 'y3', 'y4', 'z1', 'z2', 'z3', 'z4']

    def variables(self):
        vrbls = self.evidences()
        vrbls.extend(['class'])
        return vrbls

    def inInference(self):
        return 'inference/in.txt'
    
    def outInference(self):
        return 'inference/out.txt'
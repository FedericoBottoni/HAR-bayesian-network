
class Config():

    def percGetData(self):
        return 1

    def nOfBuckets(self):
        return 3

    def evidences(self):
        return ['x1', 'x2', 'x3', 'x4', 'y1', 'y2', 'y3', 'y4', 'z1', 'z2', 'z3', 'z4']

    def variables(self):
        vrbls = self.evidences()
        vrbls.extend(['class'])
        return vrbls
    
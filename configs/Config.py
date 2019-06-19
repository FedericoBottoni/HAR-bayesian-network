
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
    
    def getSavedCpds(self, varName):
        bidCpd=list()
        print('LOG: opening CPD ' + varName + '.txt"')
        f=open('generatedCPDs/' + varName + '.txt', "r", newline="\r\n", encoding="utf-8")
        data=f.read()
        f.close()
        data=data[:-1]
        data=data[1:]
        rows=data.split("]")
        for row in rows:
            newRow=list()
            cells=row.replace("\r\n", "").replace(" [", "").replace("[", "").split(" ")
            for cell in cells:
                try:
                    cell=cell.replace(" ", "").replace("\r\n", "")
                    float(cell)
                    newRow.append(float(cell))
                except ValueError:
                    pass
            if(newRow):
                bidCpd.append(newRow)
        return bidCpd
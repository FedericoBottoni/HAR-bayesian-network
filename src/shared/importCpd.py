def importCpd(varName):
    bidCpd=list()
    #print('LOG: opening CPD ' + varName + '.txt"')
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
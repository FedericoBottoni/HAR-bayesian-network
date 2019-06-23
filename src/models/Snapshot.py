# user;gender;age;how_tall_in_meters;weight;body_mass_index;x1;y1;z1;x2;y2;z2;x3;y3;z3;x4;y4;z4;class

class Snapshot():
    def __init__(self, splittedRow):
        self.x1 = splittedRow[0]
        self.y1 = splittedRow[1]
        self.z1 = splittedRow[2]
        self.x2 = splittedRow[3]
        self.y2 = splittedRow[4]
        self.z2 = splittedRow[5]
        self.x3 = splittedRow[6]
        self.y3 = splittedRow[7]
        self.z3 = splittedRow[8]
        self.x4 = splittedRow[9]
        self.y4 = splittedRow[10]
        self.z4 = splittedRow[11]
        self.harClass = splittedRow[12]
        
    def toString(self):
        return 'x1=' + str(self.x1) + ';y1=' + str(self.y1) + ';z1=' + str(self.z1) + ';x2=' + str(self.x2) + ';y2=' + str(self.y2) + ';z2=' + str(self.z2) + ';x3=' + str(self.x3) + ';y3=' + str(self.y3) + ';z3=' + str(self.z3) + ';x4=' + str(self.x4) + ';y4=' + str(self.y4) + ';z4=' + str(self.z4) + ';harClass=' + str(self.harClass)

# user;gender;age;how_tall_in_meters;weight;body_mass_index;x1;y1;z1;x2;y2;z2;x3;y3;z3;x4;y4;z4;class
import copy
from discretize import discretize

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

    def getDiscretizedInstance(self, rng):
        discInstance = copy.copy(self)
        discInstance.howTallInMeters = self.getDiscretizedHeight()
        discInstance.x1 = discretize(self.x1, rng)
        discInstance.y1 = discretize(self.y1, rng)
        discInstance.z1 = discretize(self.z1, rng)
        discInstance.x2 = discretize(self.x2, rng)
        discInstance.y2 = discretize(self.y2, rng)
        discInstance.z2 = discretize(self.z2, rng)
        discInstance.x3 = discretize(self.x3, rng)
        discInstance.y3 = discretize(self.y3, rng)
        discInstance.z3 = discretize(self.z3, rng)
        discInstance.x4 = discretize(self.x4, rng)
        discInstance.y4 = discretize(self.y4, rng)
        discInstance.z4 = discretize(self.z4, rng)
        discInstance.harClass = self.getNumberClass()
        return discInstance

    def getDiscretizedHeight(self):
        if isinstance(self.howTallInMeters, float):
            return self.howTallInMeters
        else:
            height = float(self.howTallInMeters.replace(',', '.'))
            if height <= 1.60:
                discHeight = 1.60
            elif height <= 1.65:
                discHeight = 1.65
            elif height <= 1.69:
                discHeight = 1.69
            else:
                discHeight = 1.71
            return discHeight

    def toDiscretizedString(self, rng):
        return 'user=' + str(self.user) + ';howTallInMeters=' + str(self.howTallInMeters) + ';x1=' + str(self.x1) + ';y1=' + str(self.y1) + ';z1=' + str(self.z1) + ';x2=' + str(self.x2) + ';y2=' + str(self.y2) + ';z2=' + str(self.z2) + ';x3=' + str(self.x3) + ';y3=' + str(self.y3) + ';z3=' + str(self.z3) + ';x4=' + str(self.x4) + ';y4=' + str(self.y4) + ';z4=' + str(self.z4) + ';harClass=' + str(self.harClass)

# user;gender;age;how_tall_in_meters;weight;body_mass_index;x1;y1;z1;x2;y2;z2;x3;y3;z3;x4;y4;z4;class
import copy
from discretize import discretize

class Snapshot():
    def __init__(self, splittedRow):
        self.user = splittedRow[0]
        #self.gender = splittedRow[1]
        #self.age = splittedRow[2]
        self.howTallInMeters = splittedRow[3]
        #self.weight = splittedRow[4]
        #self.bodyMassIndex = splittedRow[5]
        self.x1 = int(splittedRow[6])
        self.y1 = int(splittedRow[7])
        self.z1 = int(splittedRow[8])
        self.x2 = int(splittedRow[9])
        self.y2 = int(splittedRow[10])
        self.z2 = int(splittedRow[11])
        self.x3 = int(splittedRow[12])
        self.y3 = int(splittedRow[13])
        self.z3 = int(splittedRow[14])
        self.x4 = int(splittedRow[15])
        self.y4 = int(splittedRow[16])
        self.z4 = int(splittedRow[17])
        self.harClass = splittedRow[18]

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

    def getNumberClass(self):
        if self.harClass == 'walking':
            classNumber = 1
        elif self.harClass == 'standing':
            classNumber = 2
        elif self.harClass == 'standingup':
            classNumber = 3
        elif self.harClass == 'sitting':
            classNumber = 4
        elif self.harClass == 'sittingdown':
            classNumber = 3
        else:
            raise Exception()
        return classNumber
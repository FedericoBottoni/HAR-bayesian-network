from BasicConfig import BasicConfig

class Config(BasicConfig):
    def getRangeSize(self):
        return 5

    def getNetwork(self):
        network = super().basicUserNetwork() # basicUserNetwork || basicTallNetwork
        network.extend([
            ('y1', 'z1'), ('x2', 'y2'), ('x2', 'z2'), ('y2', 'z2'), ('y3', 'z3'), ('x4', 'z1'),  ('x4', 'y4')
        ])
        return network
        
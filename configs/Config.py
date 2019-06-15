from BasicConfig import BasicConfig

class Config(BasicConfig):
    def getRangeSize(self):
        return 2

    def getNetwork(self):
        network = super().basicUserNetwork() # basicUserNetwork || basicTallNetwork
        network.extend([
            ('x1', 'x2')
        ])
        return network
        
class Corr05ConfigBn():
    # Network got by the Paerson's correlation index |val| >= 0.5
    def getNetwork(self):
        network = super().basicUserNetwork() # basicUserNetwork || basicTallNetwork
        network.extend([
            ('y1', 'z1'), ('x2', 'y2'), ('x2', 'z2'), ('y2', 'z2'), ('y3', 'z3'), ('x4', 'z1'),  ('x4', 'y4')
        ])
        return network
        
    def getCpd(self):
        return []
        
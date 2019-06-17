class BasicConfig():

    def basicUserNetwork(self):
        return [
            ('user', 'x1'), ('user', 'x2'), ('user', 'x3'), ('user', 'x4'),
            ('user', 'y1'), ('user', 'y2'), ('user', 'y3'), ('user', 'y4'),
            ('user', 'z1'), ('user', 'z2'), ('user', 'z3'), ('user', 'z4')]

    def basicTallNetwork(self):
        return [
            ('how_tall_in_meters', 'x1'), ('how_tall_in_meters', 'x2'), ('how_tall_in_meters', 'x3'), ('how_tall_in_meters', 'x4'),
            ('how_tall_in_meters', 'y1'), ('how_tall_in_meters', 'y2'), ('how_tall_in_meters', 'y3'), ('how_tall_in_meters', 'y4'),
            ('how_tall_in_meters', 'z1'), ('how_tall_in_meters', 'z2'), ('how_tall_in_meters', 'z3'), ('how_tall_in_meters', 'z4')
        ]

    def basicNetwork(self):
        network = self.basicTallNetwork()
        network.extend([ # basicUserNetwork || basicTallNetwork
            ('x1', 'class'),                  ('x3', 'class'),
                                                               ('y4', 'class'),
            ('z1', 'class'), ('z2', 'class'), ('z3', 'class'), ('z4', 'class'),
        ])
        return network
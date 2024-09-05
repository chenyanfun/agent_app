
# define edge

class Edge:
    def __init__(self, source, target, edge_type, weight=1):
        self.source = source
        self.target = target
        self.edge_type = edge_type
        self.weight = weight

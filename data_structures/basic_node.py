# define node

class Node:
    def __init__(self, node_id, node_type, metadata, node_func, result=None):
        self.node_id = node_id
        self.node_type = node_type
        self.metadata = metadata
        self.edges = []
        self.node_func = node_func
        self.result = result

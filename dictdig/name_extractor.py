class NameExtractor:
    def __init__(self, node_name):
        self.node_name = node_name

    def extract(self, node):
        if self.node_name in node:
            return node[self.node_name]
        else:
            return None

class Vertice():
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.visited = False
        self.parent = None
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
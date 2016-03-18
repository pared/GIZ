


class Graph():
    def __init__(self, vertices):
        self.vertices = vertices

    def get_neighbors(self, vertice):
        ret = []
        for letter in vertice.neighbors:
            ret.append(self.get_vertice(letter))
        return ret

    def get_vertice(self, letter):
        for vertice in self.vertices:
            if vertice.name == letter:
                return vertice
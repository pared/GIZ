from Graph import *
from Vertice import *
from Queue import *

A = Vertice('A', ['B', 'C', 'G'])
B = Vertice('B', ['A', 'C', 'G', 'D'])
C = Vertice('C', ['B', 'D', 'F', 'A'])
D = Vertice('D', ['C', 'B', 'I'])
E = Vertice('E', ['J', 'I', 'F'])
F = Vertice('F', ['E', 'C', 'H', 'G'])
G = Vertice('G', ['F', 'H', 'A'])
H = Vertice('H', ['G', 'F', 'I', 'B'])
I = Vertice('I', ['H', 'E', 'D'])
J = Vertice('J', ['B', 'D', 'E'])

graph = Graph([A, B, C, D, E, F, G, H, I, J])
q = Queue()

# print graph.get_neighbors(A)
# print graph.get_neighbors(B)
# print graph.get_neighbors(C)
# print graph.get_neighbors(D)
# print graph.get_neighbors(E)
# print graph.get_neighbors(F)
# print graph.get_neighbors(G)
# print graph.get_neighbors(H)
# print graph.get_neighbors(I)
# print graph.get_neighbors(J)

def bsf(g, s):
    for u in g.vertices:
        u.visited = False
        u.parent = None
    s.visited = True
    print ('Visited: '+ str(s))
    s.parent = None
    q._put(s)
    while q.empty() != True:
        u = q._get()
        for v in g.get_neighbors(u):
            if v.visited == False:
                v.visited = True
                print ('After '+str(u)+ ' Visited '+ str(v))
                v.parent = u
                q._put(v)
        u.visited = True






bsf(graph, B)

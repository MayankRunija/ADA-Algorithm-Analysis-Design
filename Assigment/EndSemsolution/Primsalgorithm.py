
"""
Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. 
Here is the implementation of Prim's algorithm in Python:
"""
import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        for v in range(self.vertices):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.vertices
        parent = [None] * self.vertices
        mstSet = [False] * self.vertices

        key[0] = 0
        parent[0] = -1

        for _ in range(self.vertices):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

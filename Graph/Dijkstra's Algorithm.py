import sys

class Graph:
    def __init__(self, vetices):
        self.n = vetices
        self.graph = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self, start, end, weight):
        self.graph[start][end] = weight
        self.graph[end][start] = weight

    def print_graph(self):
        for i in self.graph:
            print(i)
        print()

    def dijkstra(self, source):
        dist = [sys.maxsize]*self.n
        visited = {source}
        dist[source] = 0
        while len(visited) < self.n:
            for i in range(self.n):
                if self.graph[source][i] > 0 and i not in visited and dist[i] > dist[source] + self.graph[source][i]:
                    dist[i] = dist[source] + self.graph[source][i]
            min_dist = sys.maxsize
            source = 0
            for i in range(self.n):
                if i not in visited and dist[i] < min_dist:
                    min_dist = dist[i]
                    source = i
            visited.add(source)
        for i in range(self.n):
            print(i,'->', dist[i])



g = Graph(9)
g.add_edge(0,1,4)
g.add_edge(0,7,8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

g.print_graph()

g.dijkstra(0)
class Graph:
    def __init__(self,vertices):
        self.n = vertices
        self.graph = [[False for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self, start, end):
        self.graph[start][end] = True
        self.graph[end][start] = True

    def print_graph(self):
        for i in self.graph:
            print(i)
        print()

    def bfs(self, source):
        added_in_queue = {source}
        queue = [source]
        while queue:
            front = queue.pop(0)
            print(front, end=" ")
            if len(added_in_queue) < self.n:
                for i in range(self.n):
                    if i not in added_in_queue and self.graph[front][i] == True:
                        queue.append(i)
                        added_in_queue.add(i)
        print()

vertices = 6
g = Graph(vertices)
g.add_edge(0,1)
g.add_edge(1,3)
g.add_edge(0,2)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(3,4)

g.print_graph()

g.bfs(0)

class Graph:
    def __init__(self,vertices):
        self.n = vertices
        self.graph = [[False for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self, start, end):
        self.graph[start-1][end-1] = True
        self.graph[end-1][start-1] = True

    def print_graph(self):
        for i in self.graph:
            print(i)
        print()

    def bfs(self, source):
        visited = [False for _ in range(self.n)]
        queue = [source-1]
        visited[source-1] = True
        while queue:
            if visited.count(False)>0:
                for i in range(self.n):
                    if visited[i] == False and self.graph[queue[0]][i] == True:
                        queue.append(i)
                        visited[i] = True
            print(queue[0]+1, end=" ")
            queue.pop(0)
        print()

vertices = 6
g = Graph(vertices)
g.add_edge(1,2)
g.add_edge(2,4)
g.add_edge(1,3)
g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(4,6)
g.add_edge(5,6)
g.add_edge(4,5)

g.print_graph()

g.bfs(1)

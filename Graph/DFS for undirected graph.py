class Graph:
    def __init__(self, vertices):
        self.n = vertices
        self.graph = [[False for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self,start,end):
        self.graph[start][end] = True
        self.graph[end][start] = True

    def print_graph(self):
        for i in self.graph:
            print(i)
        print()

    def dfs(self,source):
        visited = {source}
        stack = [source]
        while stack:
            top = stack.pop()
            print(top, end=" ")
            if len(visited) < self.n:
                for i in range(self.n-1,-1,-1):
                    if i not in visited and self.graph[top][i] == True:
                        stack.append(i)
                        visited.add(i)
        print()


vertices = 6
g = Graph(vertices)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

g.print_graph()

g.dfs(0)

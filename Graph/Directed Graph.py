import sys

class Graph:
    def __init__(self, vertices):
        self.n = vertices
        self.graph = [[False for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self,start,end):
        self.graph[start][end] = True

    def print_graph(self):
        for i in self.graph:
            print(i)

    def bfs(self, source):
        queue = [source]
        visited = [source]
        while queue:
            if len(visited) < self.n:
                for i in range(self.n):
                    if i not in visited and self.graph[queue[0]][i] == True:
                        queue.append(i)
                        visited.append(i)
            print(queue[0], end=" ")
            queue.pop(0)
        print()

    def dfs(self,source):
        visited = [source]
        stack = [source]
        while stack:
            top = stack.pop()
            print(top, end=" ")
            if len(visited) < self.n:
                for i in range(self.n - 1, -1, -1):
                    if i not in visited and self.graph[top][i] == True:
                        stack.append(i)
                        visited.append(i)
        print()

    def check_cycle(self, source):
        add_stack = {source}
        stack = [source]
        visited = set()
        while stack:
            top = stack.pop()
            visited.add(top)
            if len(add_stack) < self.n:
                for i in range(self.n - 1, -1, -1):
                    if self.graph[top][i] == True:
                        if i in visited:
                            return "Forms a cycle"
                        elif i not in add_stack:
                            stack.append(i)
                            add_stack.add(i)
        return "Does not form a cycle"

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.n
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
            print(i, '->', dist[i])
        print()


vertices = 4
g = Graph(vertices)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.print_graph()

g.bfs(0)
g.dfs(0)

print(g.check_cycle(0))

g.dijkstra(0)

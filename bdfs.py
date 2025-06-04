class Graph:
    def _init_(self):
        self.graph={}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
    def display(self):
        print("Adjacency List")
        for i in self.graph:
            print(f"{i} --> {self.graph[i]}")
    def bfs(self,start):
        visited=set()
        queue=[start]
        while queue:
            vertex=queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex,end=' ')
                for i in self.graph[vertex]:
                    if i not in visited:
                        queue.append(i)
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start,end=' ')
        for i in self.graph[start]:
            if i not in visited:
                self.dfs(i,visited)
g=Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,7)
g.display()
g.bfs(1)
print("\n Dfs")
g.dfs(1)


'''
adj_matrix=[
[0,1,1,0,0,0,0],,
[1,0,0,1,0,0,0],
[1,0,0,1,0,0,0],
[0,1,1,0,1,0,0],
[0,0,0,1,0,1,0],
[0,0,0,0,1,0,1],
[0,0,0,0,0,1,0]]'''

class GraphAdjMatrix:
    def _init_(self,size=None,adj_matrix=None):
        if adj_matrix is not None:
            self.adj_matrix=adj_matrix
            self.size=len(adj_matrix)
        else:
            self.size=size
            self.adj_matrix=[[0 for _ in range(size)] for _ in range(size)]
    def add_edge(self,u,v):
        if u<self.size and v<self.size:
            self.adj_matrix[u][v]=1
            self.adj_matrix[v][u]=1
    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))
adj_matrix=[
[0,1,1,0,0,0,0],
[1,0,0,1,0,0,0],
[1,0,0,1,0,0,0],
[0,1,1,0,1,0,0],
[0,0,0,1,0,1,0],
[0,0,0,0,1,0,1],
[0,0,0,0,0,1,0]]
g=GraphAdjMatrix(adj_matrix=adj_matrix)
g.display()
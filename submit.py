class BFS:
    # PerformBDFS on graph g starting from the source vertex s
    def __init__(self, g, s):        
        self.g, self.s = g, s
        self.visited = [False for _ in range(g.V)]
        self.fromVertex = [None for _ in range(g.V)]
        self.distance = [None for _ in range(g.V)]
        queue = Queue()
        queue.put(s)        
        self.visited[s] = True
        self.distance[s] = 0
        while queue.qsize() > 0:         
            v = queue.get()
            for w in g.adj[v]:
                if not self.visited[w]:
                    queue.put(w)
                    self.visited[w] = True
                    self.fromVertex[w] = v
                    self.distance[w] = self.distance[v] + 1

    # Return a list of vertices on the path from s to v
    def pathTo(self, v):
        if not self.visited[v]: return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.fromVertex[v]
        path.append(self.s)
        path.reverse()
        return path

    def hasPathTo(self, v):
        return self.visited[v]

    def distTo(self, v):
        return self.distance[v]
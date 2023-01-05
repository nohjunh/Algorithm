def topologicalSort(g):
    def recur(v):
      visited[v] = True
      for w in g.adj[v]:
        if not visited[w]:
          recur(w)
      result.append(v)
    visited = [False for _ in range(g.V)]
    result = []
    for v in range( g.V ):
      if not visited[v]:
        recur(v)
    result.reverse()

    return result
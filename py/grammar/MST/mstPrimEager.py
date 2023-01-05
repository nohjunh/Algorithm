# copyright sihyunglee@knu.ac.kr
def mstPrimEager(g):
    def include(w):
      included[w] = True
      for e in g.adj[w]: # w에 인접한 각 각선 w-x에 대해
        x=e.other(w)
        if not included[x]:
          if not pq.contains(x):
            pq.insert(x, e) # index, key
          else:
            if pq.keyOf(x).weight > e.weight:
              pq.decreaseKey(x, e)
    
    assert(isinstance(g, WUGraph))

    edgesInMST = [] # Stores edges selected as part of the MST
    included = [False] * g.V # included[v] == True if v is in the MST
    weightSum = 0  # Sum of edge weights in the MST    
    pq = IndexMinPQ(g.V) # Build a IndexMinPQ
    include(0) # include(0) 호출해 정점 0 에 인접한 정점을 모두 pq에 추가함

    while len(edgesInMST) < g.V-1:
      e, w = pq.delMin() # key, index
      edgesInMST.append(e)
      weightSum += e.weight
      include(w) # Add to the MST the vertex not yet included

    return edgesInMST, weightSum # EdgesInMST, Weight
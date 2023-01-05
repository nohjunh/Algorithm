# 1707 Bipartite Graph
import sys
import queue
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def BFS(s):
  q = queue.Queue()
  q.put(s)
  color[s]= 1
  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if color[v] == 0:
        if color[u] == 1:
          color[v] = 2
        else:
          color[v] = 1
        q.put(v)
      elif color[v] == color[u]:
        return False
  return True

answer= True
K= int(input())
for _ in range(K):
  V, E = map(int, input().split())
  graph = [[] for _ in range(V+1)]
  color = [0 for _ in range(V+1)] # 0이면 아직 방문 안한거, 1이면 A그룹, 2이면 B그룹
  for _ in range(E):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in range(1, V+1):
    if color[i] == 0:
      answer = BFS(i)
      if not answer:
        break
  if answer==True:
    print("YES")
  else:
    print("NO")
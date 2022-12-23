# 11657 타임머신, bellman_ford algorithm
import sys
input = sys.stdin.readline
INF = float('inf')

def bellman_ford(graph, start):
  distTo[start] = 0

  # 정점 개수만큼 반복
  for i in range(N):
    for v in range(1, N+1):
      for w, weight in graph[v]:
        if distTo[v] != INF and distTo[w] > distTo[v] + weight:
          distTo[w] = distTo[v] + weight
          edgeTo[w] = v
          if i == N-1: # 값이 갱신될 수 있다면 음의 순환 존재
            return False
  return True
          

N, M = map(int, input().split())
graph= [[] for _ in range(N+1)]
distTo= [INF] * (N+1)
edgeTo= [None] * (N+1)

for _ in range(M):
  A,B,C = map(int, input().split())
  graph[A].append((B,C))

result = bellman_ford(graph, 1)

if result == False:
  print(-1)
else:
  for i in range(2, N+1):
    if distTo[i] == INF:
      print(-1)
    else:
      print(distTo[i])
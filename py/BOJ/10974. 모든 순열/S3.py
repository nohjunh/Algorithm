# 10974. 모든 순열
from sys import stdin
input = stdin.readline

def dfs(depth, list):
  if depth == N:
    print(*list)
    return
  if depth > N:
    return
  for i in range(1, N+1):
    if visited[i] == False:
      visited[i]= True
      list.append(i)
      dfs(depth+1, list)
      visited[i]= False
      list.remove(i)
  
N = int(input())
visited = [False] * (N+1)
dfs(0, [])
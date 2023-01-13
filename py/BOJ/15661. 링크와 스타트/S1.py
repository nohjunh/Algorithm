#15661. 링크와 스타트
from sys import stdin
input = stdin.readline

def dfs(depth, idx):
  global minValue
  if depth == N:
    linkTeam= 0
    startTeam = 0
    for i in range(N):
      for j in range(N):
        if visited[i] and visited[j]:
          linkTeam += graph[i][j]
        elif not visited[i] and not visited[j]:
          startTeam += graph[i][j]
    minValue= min(minValue, abs(linkTeam-startTeam))
  if depth > N:
    return

  visited[idx] = True
  dfs(depth+1, idx+1)
  visited[idx] = False
  dfs(depth+1, idx+1)


N= int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
minValue = 1e9
visited = [False] * (N+1)

dfs(0, 0)
print(minValue)
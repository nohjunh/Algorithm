# 14889 스타트와 링크
# https://youtu.be/jKJ5SdUwI9A
from sys import stdin
input = stdin.readline

def DFS(depth, idx):
  global minAbility
  teamAability = 0
  teamBability = 0
  if depth == N//2: #팀이 나눠졌다면
    for i in range(N): # 중첩for문을 통해 S_ij + S_ji 값을 더하는 구조
      for j in range(N):
        if included[i] and included[j]:
          teamAability += graph[i][j]
        elif not included[i] and not included[j]:
          teamBability += graph[i][j]
    minAbility = min(minAbility, abs(teamAability-teamBability))
    return
  # 팀이 나눠지지 않았다면
  for idx in range(idx, N):
    if not included[idx]:
      included[idx] = True
      DFS(depth+1, idx+1)
      included[idx] = False

N= int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
included= [False]*N
minAbility=1e9

DFS(0,0)
print(minAbility)
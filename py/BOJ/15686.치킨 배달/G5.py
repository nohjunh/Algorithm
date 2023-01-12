#15686 치킨 배달
from sys import stdin
input = stdin.readline

def dfs(depth, count):
  global minPath
  if count == M:
    distance=0
    for x_house, y_house in houseXY:
      SP= 1e9
      for idx, check in enumerate(visited):
        if check == True:
          x_chicken, y_chicken = chickenXY[idx]
          SP = min(SP, abs(x_house - x_chicken) + abs(y_house - y_chicken))
      distance+= SP 
    minPath = min(minPath, distance)
    return
  if depth > len(chickenXY):
    return
  
  for idx in range(depth, len(chickenXY)):
    if visited[idx] == False:
        visited[idx]= True
        dfs(idx, count+1) # 재귀를 들어갈 때 for문의 index= 0부터 들어가는게 아니라 idx부터 들어가야 시간초과가 안 뜸
        visited[idx]= False

# N개의 줄에 도시정보
# 0= 빈 칸, 1= 집, 2= 치킨 집
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houseXY= []
chickenXY = []

for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      houseXY.append([i,j])
    elif city[i][j] == 2:
      chickenXY.append([i,j])

visited= [False] * (len(chickenXY))
minPath = 1e9

dfs(0, 0)
print(minPath)
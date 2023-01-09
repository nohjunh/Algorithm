# 9663 N-Queen
"""
depth=1 ㅁㅁㅁ  1,1 1,2 1,3    x-1 y-1     y-1     x+1 y-1
depth=2 ㅁㅁㅁ  2,1 2,2 2,3      x-1      현위치      x+1 
depth=3 ㅁㅁㅁ  3,1 3,2 3,3    x-1 y+1     y+1     x+1 y+1
"""      
from sys import stdin
input = stdin.readline

def check(depth):
  for i in range(1, depth): # 모든 depth를 돌면서 
    if row[i]==row[depth]: # 해당 depth번째 행에 Queen을 위치시켰을 때 열이 겹치는게 있는지 파악
      return False
    if abs(row[depth]-row[i]) == depth-i: # 대각선이 겹치는지 파악
      return False
  return True

def dfs(depth):
  global count
  if depth==N+1: # depth를 1부터 시작했기에 N개에 행에 Queen이 다 위치했을 때 탐색 depth는 N+1이 됨. 여기가 종료점
    count+=1
    return
  for col in range(1, N+1): # 다음 depth에서 Queen이 위치할 수 있는 범위 탐색
    if visited[col]:
      continue
    row[depth] = col # 해당 depth번째 행의 Queen은 col번째 행에 위치
    if check(depth): # 위치할 수 있는지 check
      visited[col] = True
      dfs(depth+1)
      visited[col] = False

# N = 퀸 갯수
N= int(input())
row = [0]*(N+1) # 구현의 편리함을 위함
# ex) row[3] => 1 이면 3번째 행에 Queen은 1번째 열에 위치한다는 뜻
count = 0
visited= [False]*(N+1)
dfs(1)
print(count)
#1987 알파벳
from sys import stdin
input = stdin.readline
# list의 append, remove 함수를 쓰면 시간초과가 나오기 때문에
# 아스키코드를 계산해서 수행

def dfs(X, Y, count):
  global maxCount
  
  maxCount = max(maxCount, count)

  for i in range(4):
    nx = X + dx[i]
    ny = Y + dy[i]
    
    if 0 <= nx < R and 0 <= ny < C and visited[ord(graph[nx][ny]) - 65] == False:
      visited[ord(graph[nx][ny]) - 65] = True
      dfs(nx, ny, count+1)
      visited[ord(graph[nx][ny]) - 65] = False

dx = [1, -1, 0, 0]
dy = [0,  0, 1, -1]
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [False] * (26) # 알파벳 갯수
maxCount= -1e9

# x좌표, y좌표, 최대 칸 수
  # 스타트 최상단은 넣어주고 시작
visited[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)
print(maxCount)
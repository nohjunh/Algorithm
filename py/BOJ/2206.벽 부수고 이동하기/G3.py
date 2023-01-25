# 2206. 벽 부수고 이동하기
"""
구현 상 벽을 이미 뚫은 곳을 벽을 안뚫은 상태(state==0)로 가게 되는 경우
한번 더 뚫게 되는 경우가 발생한다. 그러나, state가 1로 변경됐고
state가 1인 상태로 이미 그 곳을 지났기에 queue에서 pop한 후 4방향
탐색을 할 때 이미 visited 되어서 더 이상 진행되지 않게 됨.
즉, 결국에는 간 곳을 더이상 가지 않는 BFS 성립.
"""
import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y, wallState): # wall이 1이면 벽을 부순 상태, 0이면 아직 벽을 안부순 상태
  queue = deque()
  queue.append( (x, y, wallState) )
  visited[x][y][wallState] = 1 # 처음은 벽은 안부순 상태에서 시작
  
  while queue:
    curX, curY, state = queue.popleft()
    
    if curX == N-1 and curY == M-1:
      return visited[curX][curY][state]
    
    for i in range(4):
      nx = curX + dx[i]
      ny = curY + dy[i]
      if 0 <= nx < N  and 0 <= ny < M:
        # 벽이 아니고, 방문 안한 곳이면 (방문 한 곳이면 그냥 넘어감)
        if graph[nx][ny] == 0 and visited[nx][ny][state] == 0:
          visited[nx][ny][state] = visited[curX][curY][state] + 1 # 거리증가
          queue.append( (nx, ny, state) )
        # 벽이면서, 아직 벽을 파괴한 적이 없다면 (벽을 파괴한 적이 있으면 그냥 넘어감)
        elif graph[nx][ny] == 1 and state == 0:
            visited[nx][ny][1] = visited[curX][curY][0] + 1
            queue.append( (nx, ny, 1) )
  return -1 # 최단 거리를 찾지 못한 경우


# N X M 행렬
N, M =map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# [x][y][0] == 아직 벽을 안 부순 경우, [x][y][1] == 벽을 부순 경우
# visited 배열로 거리와 방문여부를 판단
visited = [ [[0,0] for _ in range(M)] for i in range(N) ]

print(BFS(0, 0, 0))
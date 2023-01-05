# 10026 적록색약 
import sys
from collections import deque
input= sys.stdin.readline

# N= 그리드 크기 
N= int(input())
graph_matrix = [list(input().rstrip()) for _ in range(N)]

# 4방향검사
dx=[0,0,1,-1]
dy=[1,-1,0,0]

# 빨간색과 초록색의 차이를 느끼지 못하는 적록색약 함수문
def RG_BFS_adj_list(graph_matrix, first_x, first_y):
    queue= deque()
    queue.append((first_x,first_y))
    visited[first_x][first_y]=1 # 방문 체크
    while queue:
        x,y = queue.popleft()
        if graph_matrix[x][y]=='R' or graph_matrix[x][y]=='G':
          # 4방향 검사
          for i in range(4):
              nx= x+dx[i]
              ny= y+dy[i]
              if 0<= nx < N and 0<= ny< N:
                  if visited[nx][ny]==0: # 방문을 안했다면
                    if graph_matrix[nx][ny]=='R' or graph_matrix[nx][ny]=='G':
                        visited[nx][ny]=1 #방문체크
                        queue.append((nx,ny))
        else: # 'B'라는 거니까
          #4방향 검사
          for i in range(4):
              nx= x+dx[i]
              ny= y+dy[i]
              if 0<= nx < N and 0<= ny< N:
                  if visited[nx][ny]==0: # 방문을 안했다면
                    if graph_matrix[nx][ny]=='B':
                        visited[nx][ny]=1 #방문체크
                        queue.append((nx,ny))

# 적록색약이 아닌 사람이 보는 그림
def RGB_BFS_adj_list(graph_matrix, first_x, first_y):
    queue= deque()
    queue.append((first_x,first_y))
    visited[first_x][first_y]=1 # 방문 체크
    while queue:
        x,y = queue.popleft()
        if graph_matrix[x][y]=='R':
          # 4방향 검사
          for i in range(4):
              nx= x+dx[i]
              ny= y+dy[i]
              if 0<= nx < N and 0<= ny< N:
                  if visited[nx][ny]==0: # 방문을 안했다면
                    if graph_matrix[nx][ny]=='R':
                        visited[nx][ny]=1 #방문체크
                        queue.append((nx,ny))
        elif graph_matrix[x][y]=='B': # 'B'라면
          #4방향 검사
          for i in range(4):
              nx= x+dx[i]
              ny= y+dy[i]
              if 0<= nx < N and 0<= ny< N:
                  if visited[nx][ny]==0: # 방문을 안했다면
                    if graph_matrix[nx][ny]=='B':
                        visited[nx][ny]=1 #방문체크
                        queue.append((nx,ny))
        else: # 'G'
          #4방향 검사
          for i in range(4):
              nx= x+dx[i]
              ny= y+dy[i]
              if 0<= nx < N and 0<= ny< N:
                  if visited[nx][ny]==0: # 방문을 안했다면
                    if graph_matrix[nx][ny]=='G':
                        visited[nx][ny]=1 #방문체크
                        queue.append((nx,ny))


# 적록색약이 보는 그림 
visited=[[0]*(N) for _ in range(N)] # 방문체크
count=0
for i in range(N):
  for j in range(N):
    if visited[i][j]==0:
      count+=1
      visited[i][j]=1
      RGB_BFS_adj_list(graph_matrix, i, j)
print(count, end=' ')

# 적록색약이 아닌 사람이 보는 그림
visited=[[0]*(N) for _ in range(N)] # 방문체크
count=0
for i in range(N):
  for j in range(N):
    if visited[i][j]==0:
      count+=1
      visited[i][j]=1
      RG_BFS_adj_list(graph_matrix, i, j)
print(count)
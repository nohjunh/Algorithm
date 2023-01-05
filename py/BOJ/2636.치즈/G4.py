# 2636 치즈
import sys
from collections import deque
input= sys.stdin.readline

# N= 사각형 모양 판의 세로
# M= 사각형 모양 판의 가로 
N,M = map(int, input().split())
graph_matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 4방향검사
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS_adj_list(graph_matrix, first_x, first_y):
    visited= [[False]*(M) for _ in range(N)]
    queue= deque()
    queue.append((first_x,first_y))
    visited[first_x][first_y]= True
    count=0
    while queue:
        x,y = queue.popleft()
        # 4방향 검사
        for i in range(4):
          nx= x+dx[i]
          ny= y+dy[i]
          if 0<= nx < N and 0<= ny< M and visited[nx][ny]==False:
              if graph_matrix[nx][ny]== 1: # 치즈가 있는 칸이면
                visited[nx][ny]= True
                graph_matrix[nx][ny]=0  # 치즈가 녹았음을 표현
                count+=1
              elif graph_matrix[nx][ny]== 0: # 치즈가 없는 칸이면
                visited[nx][ny]= True
                queue.append((nx,ny))
    result.append(count)
    return count # count는 그 단계에서 몇 개의 치즈가 녹았는지를 판단해줌.

result= []
time_cheese=0
# 치즈 위치가 0이면 큐에 넣어서 BFS 돌리고 
# 1을 만날 때마다 0으로 바꿔주면서 time 증가시키면 가장자리부터 처리되는거
while True:
  count= BFS_adj_list(graph_matrix, 0, 0)
  if count==0:
    break
  time_cheese+=1

print(time_cheese) 
# 마지막은 count가 0일테니까 마지막 그 전을 출력
print(result[len(result)-2])
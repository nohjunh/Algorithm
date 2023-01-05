# 7576
import sys
input=sys.stdin.readline
from collections import deque

# M,N 상자의 크기
# M= 상자의 가로 칸 수
# N= 상자의 세로 칸 수
M,N =map(int, input().split())

graph_matrix=[list(map(int, input().split())) for _ in range(N)]

def BFS_adj_list(one_list):
    queue= deque() # 큐 선언
    for i in one_list:
        queue.append(i)
    while queue:
        x, y = queue.popleft()
        # 4방향을 검사
        # 단 익은 Day는 -1을 해줘야 정확함. -> 첫 시작 토마토 값이 1부터 시작하기 때문
        if (x+1 < N)  and (graph_matrix[x+1][y]== 0):
            graph_matrix[x+1][y]= graph_matrix[x][y]+1 # 해당 좌표의 토마토가 익은 day
            queue.append( (x+1, y) )
        if (x-1 >= 0)  and (graph_matrix[x-1][y]== 0):
            graph_matrix[x-1][y]= graph_matrix[x][y]+1 # 해당 좌표의 토마토가 익은 day
            queue.append( (x-1, y) )
        if ( y+1 < M) and (graph_matrix[x][y+1]==0):
            graph_matrix[x][y+1]= graph_matrix[x][y]+1 # 해당 좌표의 토마토가 익은 day
            queue.append( (x, y+1) )
        if( y-1 >= 0) and (graph_matrix[x][y-1]== 0):
            graph_matrix[x][y-1]= graph_matrix[x][y]+1 # 해당 좌표의 토마토가 익은 day
            queue.append( (x, y-1) )

one_list= []
for i in range(N):
    for j in range(M):
        if graph_matrix[i][j]== 1:
            one_list.append( (i,j) )
BFS_adj_list(one_list)
ans=0
for i in range(N):
    for j in range(M):
        if graph_matrix[i][j]==0:
            print(-1)
            exit()
        else:
            ans= max(graph_matrix[i][j], ans)

# 그래프의 시작은 1부터 시작하는 반면 Day는 0->1일 부터 번지는 것을 고려해서 -1을 해준다.
print(ans-1)
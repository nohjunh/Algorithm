# 2178
import sys
from collections import deque
input= sys.stdin.readline

# N= N개의 줄 , M= M개의 정수 로 (N,M)으로 미로
N, M = map(int, input().split()) 
graph_matrix = [[]*(M) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)] # visited이 0이면 아직 방문하지않은거

# 미로 정보 받아오기
for i in range(N):
    M_list= input().rstrip()
    for j in range(len(M_list)):
        graph_matrix[i].append(int(M_list[j]))

def BFS_with_adj_list(graph_matrix, first_x, first_y):
    queue= deque( [(first_x, first_y)] ) # 큐 선언
    visited[first_x][first_y]= 1 # 1,1부터 시작 -> 방문했다고 처리
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y==M-1:
            print(visited[x][y])
            break

        # 4방향을 검사
        if (x+1 < N) and (visited[x+1][y] == 0) and (graph_matrix[x+1][y]== 1):
            visited[x+1][y]= visited[x][y]+ 1 # 한칸 이동했으므로 이동횟수 +1
            queue.append( (x+1, y) )
        if (x-1 >= 0) and (visited[x-1][y] == 0) and (graph_matrix[x-1][y]== 1):
            visited[x-1][y]= visited[x][y]+ 1
            queue.append( (x-1, y) )
        if ( y+1 < M) and (visited[x][y+1] == 0) and (graph_matrix[x][y+1]==1):
            visited[x][y+1] = visited[x][y]+ 1
            queue.append( (x, y+1) )
        if( y-1 >= 0) and (visited[x][y-1] == 0) and (graph_matrix[x][y-1]== 1):
            visited[x][y-1] = visited[x][y]+ 1
            queue.append( (x, y-1) )   

BFS_with_adj_list(graph_matrix, 0, 0)


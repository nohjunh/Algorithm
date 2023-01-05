# 2667
import sys
input=sys.stdin.readline
from collections import deque

# N= 지도의 크기
N=int(input())

graph_matrix = [[]*(N) for _ in range(N)]

# 지도 정보 받아오기
for i in range(N):
    N_list= input().rstrip()
    for j in range(len(N_list)):
        graph_matrix[i].append(int(N_list[j]))

visited= [[0]*(N) for _ in range(N)] # 0이면 아직 방문 안한거

def BFS_with_adj_list(graph_matrix, first_x, first_y):
    home_count=1
    queue= deque( [(first_x, first_y)] ) # 큐 선언
    if graph_matrix[first_x][first_y]==1: # 1로 집이 있고
        if visited[first_x][first_y]==0: # 방문하지 않았다면
            visited[first_x][first_y]=1 # 방문처리
            while queue:
                x, y = queue.popleft()

                # 4방향을 검사
                if (x+1 < N) and (visited[x+1][y] == 0) and (graph_matrix[x+1][y]== 1):
                    visited[x+1][y]=1 #방문처리
                    home_count+=1
                    queue.append( (x+1, y) )
                if (x-1 >= 0) and (visited[x-1][y] == 0) and (graph_matrix[x-1][y]== 1):
                    visited[x-1][y]=1 #방문처리
                    home_count+=1
                    queue.append( (x-1, y) )
                if ( y+1 < N) and (visited[x][y+1] == 0) and (graph_matrix[x][y+1]==1):
                    visited[x][y+1]= 1 #방문처리
                    home_count+=1
                    queue.append( (x, y+1) )
                if( y-1 >= 0) and (visited[x][y-1] == 0) and (graph_matrix[x][y-1]== 1):
                    visited[x][y-1]= 1 #방문처리
                    home_count+=1
                    queue.append( (x, y-1) )
            return home_count
    return 0

home_list=[]
for i in range(N):
    for j in range(N):
        if graph_matrix[i][j]== 1:
            home_list.append(BFS_with_adj_list(graph_matrix, i, j))

home_list.sort()
home_ans= []
count_ans= 0
for i in range(len(home_list)):
    if home_list[i] != 0:
        count_ans += 1
        home_ans.append(home_list[i])

print(len(home_ans))
for i in range(len(home_ans)):
    print(home_ans[i])
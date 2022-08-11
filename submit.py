# 1012
import sys
input=sys.stdin.readline
from collections import deque

# T= 테스트 케이스의 개수
T=int(input())

for _ in range(T):
    # M=가로길이, N= 세로길이, K= 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())
    graph_matrix = [[0]*(M) for _ in range(N)]
    # 배추가 심어져 있는 땅 정보 받아오기
    for i in range(K):
        x,y= map(int, input().split())
        graph_matrix[y][x]= 1

    visited= [[0]*(M) for _ in range(N)] # 0이면 아직 방문 안한거
    def BFS_with_adj_list(graph_matrix, first_x, first_y):
        earthworms_count= 1
        queue= deque( [(first_x, first_y)] ) # 큐 선언
        if graph_matrix[first_x][first_y]==1: # 1로 배추가 있고
            if visited[first_x][first_y]==0: # 방문하지 않았다면
                visited[first_x][first_y]=1 # 방문처리
                while queue:
                    x, y = queue.popleft()

                    # 4방향을 검사로 1인 땅과 탐색이 가능한 땅이면 같은 모집단이고 count를 증가시키며 방문처리함.
                    if (x+1 < N) and (visited[x+1][y] == 0) and (graph_matrix[x+1][y]== 1):
                        visited[x+1][y]=1 #방문처리
                        earthworms_count+=1
                        queue.append( (x+1, y) )
                    if (x-1 >= 0) and (visited[x-1][y] == 0) and (graph_matrix[x-1][y]== 1):
                        visited[x-1][y]=1 #방문처리
                        earthworms_count+=1
                        queue.append( (x-1, y) )
                    if ( y+1 < M) and (visited[x][y+1] == 0) and (graph_matrix[x][y+1]==1):
                        visited[x][y+1]= 1 #방문처리
                        earthworms_count+=1
                        queue.append( (x, y+1) )
                    if( y-1 >= 0) and (visited[x][y-1] == 0) and (graph_matrix[x][y-1]== 1):
                        visited[x][y-1]= 1 #방문처리
                        earthworms_count+=1
                        queue.append( (x, y-1) )
                return earthworms_count
        return 0

    ground_list=[]
    # M*N 땅을 돌면서 1인 땅이 있으면 그 땅부터 BFS탐색
    for i in range(N):
        for j in range(M):
            if graph_matrix[i][j]== 1:
                ground_list.append(BFS_with_adj_list(graph_matrix, i, j))

    ground_list.sort()
    ground_ans= []
    count_ans= 0
    # 모집단에 속한 것만 색출하기 위함.
    for i in range(len(ground_list)):
        if ground_list[i] != 0:
            count_ans += 1
            ground_ans.append(ground_list[i])
    print(count_ans)
# 14502 연구소
import sys
from collections import deque
import copy
input= sys.stdin.readline
# N= 연구소의 세로 크기
# M= 연구소의 가로 크기
N, M= map(int, input().split())
graph_matirx = [list(map(int, input().split())) for _ in range(N)]

# 4방향 탐색
dx= [0, 0, 1, -1]
dy= [1, -1, 0, 0]

def BFS_adj_list():
    queue= deque()
    # matrix 복사
    wall_graph_matrix= copy.deepcopy(graph_matirx)
    for i in range(N):
        for j in range(M):
            if wall_graph_matrix[i][j]==2:
                queue.append( (i,j) )
    while queue:
        x,y = queue.popleft()
        # 4방향 검사
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            # 연구소 지도 크기 범위 검사
            # nx가 2차원 배열에 1요소이므로 세로크기를 나타냄
            # [nx][ny] => [세로][가로] => N=세로, M=가로
            if 0<= nx < N and 0<= ny< M:
                if wall_graph_matrix[nx][ny]==0:
                    wall_graph_matrix[nx][ny]=2
                    queue.append((nx,ny))
    zero_count=0
    for i in range(N):
        for j in range(M):
            if wall_graph_matrix[i][j]==0:
                zero_count+=1
    ans_list.append(zero_count)


def wall(wall_count):
    # 재귀를 통해 빈 공간을 탐색하는 것은
    # 직접 패드로 인덱스 따라 그려보며 판단하기.
    if wall_count==3:
        BFS_adj_list()
        return
    else:
        for i in range(N):
            for j in range(M):
               if graph_matirx[i][j]==0:
                    # 길에 벽을 만듬
                    graph_matirx[i][j]=1
                    # wall_count는 재귀별로 고정일 것임.
                    # 첫번 째 재귀에서는 count=1이고
                    # 두번 째 재귀에서는 count=2
                    # 세번 째 재귀에서는 count=3
                    # 세번 째 재귀가 끝나면 count=2가 되니 
                    # 두번 째 벽의 값을 바꾸고 다시 세번 째 재귀문 호출
                    # 반복
                    wall(wall_count+1)
                    graph_matirx[i][j]=0
                    

    
ans_list=[]
wall(0)
print(max(ans_list))
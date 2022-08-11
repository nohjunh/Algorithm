# 7562
import sys
input=sys.stdin.readline
from collections import deque

def BFS_adj_list(graph_matrix, x, y):
    queue= deque() # 큐 선언
    queue.append( (x,y) )
    while queue:
        x, y= queue.popleft()
        # 8방향을 검사 ....
        if x==x_final and y==y_final:
            print(graph_matrix[x][y])
            return
        if (0<= x+2 < I) and (I> y+1 >=0) and (graph_matrix[x+2][y+1]==0):
            graph_matrix[x+2][y+1]= graph_matrix[x][y]+1 
            queue.append( (x+2, y+1) )
        if (0<= x+1 < I) and ( I > y+2 >=0 )and (graph_matrix[x+1][y+2]==0):
            graph_matrix[x+1][y+2]= graph_matrix[x][y]+1 
            queue.append( (x+1, y+2) )
        if I> x-2 >= 0 and 0<= y+1 < I and (graph_matrix[x-2][y+1]==0):
            graph_matrix[x-2][y+1]= graph_matrix[x][y]+1 
            queue.append( (x-2, y+1) )
        if I> x-1 >= 0 and 0<= y+2 < I and (graph_matrix[x-1][y+2]==0):
            graph_matrix[x-1][y+2]= graph_matrix[x][y]+1 
            queue.append( (x-1, y+2) )
        if I> x-2 >= 0 and I> y-1 >= 0 and (graph_matrix[x-2][y-1]==0):
            graph_matrix[x-2][y-1]= graph_matrix[x][y]+1 
            queue.append( (x-2, y-1) )
        if I> x-1 >= 0 and I> y-2 >= 0 and (graph_matrix[x-1][y-2]==0):
            graph_matrix[x-1][y-2]= graph_matrix[x][y]+1 
            queue.append( (x-1, y-2) )
        if 0<= x+2 < I and I> y-1 >= 0 and (graph_matrix[x+2][y-1]==0):
            graph_matrix[x+2][y-1]= graph_matrix[x][y]+1 
            queue.append( (x+2, y-1) )
        if 0<= x+1 < I and I> y-2 >= 0 and (graph_matrix[x+1][y-2]==0):
            graph_matrix[x+1][y-2]= graph_matrix[x][y]+1 
            queue.append( (x+1, y-2) )    

# T= 테스트 케이스의 개수
# I= 체스판의 한 변의 길이 -> 체스판의 크기는 2I
T=int(input())
for _ in range(T):
    I=int(input().rstrip())
    # 나이트가 현재 있는 곳
    x_current, y_current= map(int, input().split())
    # 나이트가 이동하려고 하는 칸의 정보
    x_final, y_final= map(int, input().split())

    # I x I 크기 체스판 
    graph_matrix=[[0]*(I)for _ in range(I)]
    BFS_adj_list(graph_matrix, x_current, y_current)
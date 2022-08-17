# 2583 영역 구하기
import sys
from collections import deque
input= sys.stdin.readline
# M= 모눈종이의 세로 크기
# N= 모눈종이의 가로 크기
# K= 모눈종이 위에 K개의 직사각형
M,N,K= map(int, input().split())
graph_matrix = [[0]*(N) for _ in range(M)]

# 4방향검사
dx=[0,0,1,-1]
dy=[1,-1,0,0]

# ex) (0,2), (4,4)
# ex) 4-0, 4-2 = 4(가로길이), 2(세로길이)
for _ in range(K):
  left_x, left_y, right_x, right_y= map(int, input().split())
  for i in range(left_y, right_y): #세로길이 범위
    for j in range(left_x, right_x): #가로길이 범위
      graph_matrix[(M-1)-i][j]=1


def BFS_adj_list(graph_matrix, first_x, first_y):
    queue= deque()
    queue.append((first_x,first_y))
    graph_matrix[first_x][first_y]=1 #방문 체크
    count=1 # 위에서 방문체크 먼저 해줬으므로 1부터 시작.
    while queue:
        x,y = queue.popleft()
        # 4방향 검사
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<= nx < M and 0<= ny< N:
                if graph_matrix[nx][ny]==0:
                    graph_matrix[nx][ny]=1 #방문체크
                    count+=1
                    queue.append((nx,ny))
    return count

splitAreaCount=0
splitAreaCount_list=[]

for i in range(M):
  for j in range(N):
    if graph_matrix[i][j]==0:
      splitAreaCount+=1
      splitAreaCount_list.append(BFS_adj_list(graph_matrix, i, j))

print(splitAreaCount)
splitAreaCount_list.sort()
for i in range(len(splitAreaCount_list)):
  if splitAreaCount_list[i]!=0:
    print(splitAreaCount_list[i], end=' ')
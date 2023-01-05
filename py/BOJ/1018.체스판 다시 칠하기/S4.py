# 1018 체스판 다시 칠하기
import sys
input= sys.stdin.readline
from collections import deque

N,M = map(int, (input().split()))
graph_matrix=[]
for i in range(N):
  graph_matrix.append(list(input().rstrip()))

ans=[]

for i in range(N-7):
  for j in range(M-7):
    index1=0 # 왼쪽 맨 위가 W일때 바꿔야할 체스판 갯수
    index2=0 # 왼쪽 맨 위가 B일때 바꿔야할 체스판 갯수
    # 이 2가지 경우를 index1, index2를 통해 한번의 이중 for문으로 바꿔야할 체스판의 갯수를 동시에 구할 것이다. 
    for a in range(i, i+8): #세로
      for b in range(j, j+8): #가로
        # 현재 행,열의 번호 a,b의 합이 짝수일 경우 시작점과 색이 같아야 함.
        # 현재 행,열의 번호 a,b의 합이 홀수일 경우 시작점과 색이 달라야 함.
        if (a+b)%2==0: # 짝수이니까 시작점과 색이 같아야 함.
          if graph_matrix[a][b] != 'B':
            index1+=1
          if graph_matrix[a][b] != 'W':
            index2+=1
        else:
          if graph_matrix[a][b] != 'W':
            index1+=1
          if graph_matrix[a][b] != 'B':
            index2+=1
    ans.append(min(index1,index2))

print(min(ans))
# 1012
import sys
input=sys.stdin.readline
from collections import deque

# T= 테스트 케이스의 개수
T=int(input())

# M=가로길이, N= 세로길이, K= 배추가 심어져 있는 위치의 개수
M, N, K = map(int, input().split())
graph_matrix = [[0]*(M) for _ in range(N)]
print(graph_matrix)
# 배추가 심어져 있는 땅 정보 받아오기
for i in range(K):
    x,y= map(int, input().split())
    graph_matrix[9][6]= 1

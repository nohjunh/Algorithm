# 11403
import sys
input= sys.stdin.readline

# N= 정점(노드)의 갯수
N= int(input())
# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
graph_matrix=[list(map(int, input().rstrip().replace(" ", ""))) for _ in range(N)]

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(0, N): # 거쳐가는 정점
    for i in range(0, N): # 시작 정점
        for j in range(0, N): # 도착 정점
            if graph_matrix[i][k]==1 and graph_matrix[k][j]==1:
                graph_matrix[i][j]=1

for i in range(N):
    for j in range(N):
        print(graph_matrix[i][j], end=" ")
    print()
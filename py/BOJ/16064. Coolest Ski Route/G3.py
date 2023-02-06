# 16064. Coolest Ski Route
import sys
input = sys.stdin.readline
INF = 1e9

# n= connecting points, m= number of slopes
n, m = map(int, input().split())
graph_matrix=[[INF]*(n+1) for _ in range(n+1)] # 0번 인덱스는 사용하지 않음

for _ in range(m):
    # s= point's start, t= point's end, c= condition measure
    s, t, c = map(int, input().split())
    graph_matrix[s][t] = min(graph_matrix[s][t], -c)

for k in range(1, n+1): # 거쳐가는 정점
    for i in range(1, n+1): # 시작 정점
        if graph_matrix[i][k] == INF:
            continue
        for j in range(1, n+1): # 도착 정점
            if graph_matrix[k][j] == INF:
              continue
            # i에서 j로 바로 가는 것보다 i에서 k + k에서 j로 가는 값 중 더 작은 값을 i에서 j로 가는 경로의 값으로 설정
            graph_matrix[i][j]= min(graph_matrix[i][j], graph_matrix[i][k] + graph_matrix[k][j])

print(-min(map(min, graph_matrix)))
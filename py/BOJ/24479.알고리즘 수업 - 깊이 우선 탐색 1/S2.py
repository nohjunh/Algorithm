# 24479
import sys
from collections import deque
input= sys.stdin.readline
sys.setrecursionlimit(100000)

# N=정점의 개수, M=간선의 개수, R= 탐색할 정점의 번호
N, M, V = map(int, input().split())
graph_test = [[] for _ in range(N+1)]

# 무방향 연결 = 양방향 간선
for i in range(M):
    node1, node2= map(int, input().split())
    graph_test[node1].append(node2)
    graph_test[node2].append(node1)

for i in range(len(graph_test)):
    graph_test[i].sort()

count=1
def DFS_with_adj_list(graph_test, root):
    global count
    visited[root]=count
    for node in graph_test[root]:
        if visited[node]==0:
            count+=1
            DFS_with_adj_list(graph_test, node)
    return

visited = [0 for _ in range(N+1)]
DFS_with_adj_list(graph_test, V)
for i in range(1,N+1):
    print(visited[i])
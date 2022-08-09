#24480
from lib2to3.refactor import get_fixers_from_package
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

# N개의 정점, M개의 간선, R=시작정점
N, M, R= map(int, input().split())

graph_list = [[] for _ in range(N+1)]

# 양방향 간선
for i in range(M):
    node1, node2 = map(int, input().split())
    graph_list[node1].append(node2)
    graph_list[node2].append(node1)

for i in range(1, N+1):
    graph_list[i].sort(reverse=True)

visited=[0 for _ in range(N+1)]

count=1
def DFS_adj_list(graph_list, root):
    global count
    visited[root]=count
    for node in graph_list[root]:
        if visited[node]==0:
            count+=1
            DFS_adj_list(graph_list, node)
    return visited

DFS_adj_list(graph_list, R)

for i in range(1, N+1):
    print(visited[i])

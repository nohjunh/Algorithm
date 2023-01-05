# 1260
import sys
from collections import deque
input= sys.stdin.readline

# N=정점의 개수, M=간선의 개수, V= 탐색할 정점의 번호
N, M, V = map(int, input().split())
graph_test = [[] for _ in range(N+1)]
graph_list = dict()

# 양방향 연결
for i in range(M):
    node1, node2= map(int, input().split())
    graph_test[node1].append(node2)
    graph_test[node2].append(node1)

for i in range(len(graph_test)):
    graph_test[i].sort()
    
for i in range(1,N+1):
    if len(graph_test[i])==0:
        graph_list[i]=None
    else:
        graph_list[i]=set(graph_test[i])
        
def DFS_with_adj_list(graph_list, root):
    visited.append(root)
    if graph_list[root]==None:
        return
    for node in graph_list[root]:
        if node not in visited:
            DFS_with_adj_list(graph_list, node)
    return visited

def BFS_with_adj_list(graph_list, root):
    queue= deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if graph_list[n]==None:
                continue
            queue+=graph_list[n]-set(visited)
    return visited

visited = []
DFS_with_adj_list(graph_list, V)
for i in visited:
    print(i, end=' ')

print()

visited = []
BFS_with_adj_list(graph_list, V)
for i in visited:
    print(i, end=' ')
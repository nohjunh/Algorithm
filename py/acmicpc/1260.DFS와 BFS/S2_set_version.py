# 1260
import sys
from collections import deque
input= sys.stdin.readline

# N=정점의 개수, M=간선의 개수, V= 탐색할 정점의 번호
N, M, V = map(int, input().split())
graph_test = [[] for _ in range(N+1)]

# 양방향 연결
for i in range(M):
    node1, node2= map(int, input().split())
    graph_test[node1].append(node2)
    graph_test[node2].append(node1)

for i in range(len(graph_test)):
    graph_test[i].sort()
        
def DFS_with_adj_list(graph_test, root):
    visited.add(root)
    print(root, end=' ')
    if graph_test[root]==None:
        return
    for node in graph_test[root]:
        if node not in visited:
            DFS_with_adj_list(graph_test, node)
    return visited

def BFS_with_adj_list(graph_test, root):
    queue= deque([root])
    visited.add(root)
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for neigh in graph_test[n]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)
    return visited

visited = set()
DFS_with_adj_list(graph_test, V)

print()

visited = set()
BFS_with_adj_list(graph_test, V)
# 24445
import sys
input=sys.stdin.readline
from collections import deque
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
    graph_list[i].sort(reverse= True)

visited=[0 for _ in range(N+1)]

count=1
def BFS_adj_list(graph_list, root):
    global count
    queue= deque([root])
    visited[root]=count
    while queue:
        n= queue.popleft()
        for neigh in graph_list[n]:
            if visited[neigh]== 0: # 여기서 vistied[neigh]==0 이라면 방문 안했다는거니까 방문해줘야 함.
                count+=1
                visited[neigh]=count
                queue.append(neigh)
    return visited

BFS_adj_list(graph_list, R)

for i in range(1, N+1):
    print(visited[i])
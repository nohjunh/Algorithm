import sys
from collections import deque
input= sys.stdin.readline

# 노드의 개수 N
N= int(input())
graph_matrix= [[]for _ in range(N+1)]
ans=[0]*(N+1)

# 양방향 연결
for i in range(N-1):
    node1, node2= map(int, input().split())
    graph_matrix[node1].append(node2)
    graph_matrix[node2].append(node1)

def BFS_with_adj_list(graph_matrix, root):
  queue= deque([root])
  visited.add(root)
  while queue:
      n = queue.popleft()
      for neigh in graph_matrix[n]:
          if neigh not in visited:
            ans[neigh]=n
            visited.add(neigh)
            queue.append(neigh)

visited = set()
BFS_with_adj_list(graph_matrix, 1)
for i in range(2,N+1):
  print(ans[i])

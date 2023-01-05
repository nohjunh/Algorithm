# 11724 연결 요소의 개수
import sys
from collections import deque
input= sys.stdin.readline
# N=정점의 개수, M=간선의 개수
N, M= map(int, input().split())
# 노드 번호가 1부터 주어지므로 N+1
graph_test = [[] for _ in range(N+1)]
visited= [False]*(N+1)

# 무방향이므로 양방향 연결
for i in range(M):
    node1, node2= map(int, input().split())
    graph_test[node1].append(node2)
    graph_test[node2].append(node1)

def BFS_with_adj_list(graph_test, root):
    queue= deque([root])
    visited[root]=True
    while queue:
        n = queue.popleft()
        for neigh in graph_test[n]:
            if visited[neigh]==False:
                visited[neigh]=True
                queue.append(neigh)

count=0
for i in range(1,N+1):
    if not visited[i]:
        BFS_with_adj_list(graph_test, i)
        count+=1

print(count)
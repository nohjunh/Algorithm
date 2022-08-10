# 2606
import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

# N= 컴퓨터의 수 
# M= 컴퓨터 쌍의 수(간선)
# R= 시작 컴퓨터는 1
N=int(input())
M=int(input())

graph_list = [[] for _ in range(N+1)]

# 양방향 간선
for i in range(M):
    node1, node2 = map(int, input().split())
    graph_list[node1].append(node2)
    graph_list[node2].append(node1)

visited= set()
count=0 #1번이 걸린거는 제외하고 생각! -> 1번에 의해 걸린 컴퓨터의 수를 세면 됨.
def BFS_adj_list(graph_list, root):
    global count
    queue= deque([root])
    visited.add(root)
    while queue:
        n= queue.popleft()
        for neigh in graph_list[n]:
            if neigh not in visited: # 여기서 vistied[neigh]==0 이라면 방문 안했다는거니까 방문해줘야 함.
                count+=1
                visited.add(neigh)
                queue.append(neigh)
    return visited

BFS_adj_list(graph_list, 1)
print(count)
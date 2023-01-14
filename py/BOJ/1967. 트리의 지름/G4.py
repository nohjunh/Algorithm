# 1967. 트리의 지름
"""
dfs 2번을 돌려 -> 매 dfs마다 가장 먼 거리에 있는 노드를
찾으면 되는 문제
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cur_point, totalWeight):
  # 현재 노드와 간선으로 연결된 모든 노드 방문
  for point in graph[cur_point]:
    node, weight = point
    if distance[node] == -1: # 방문 안했다면,
      distance[node] = totalWeight + weight # 지금까지의 거리에 해당 노드까지의 간선거리를 합하면 됨.
      dfs(node, distance[node])

# 노드의 갯수
n= int(input())
# 트리 그래프 구현
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  parent, child, weight = map(int, input().split())
  graph[parent].append([child, weight])
  graph[child].append([parent, weight])

"""
루트에서 가장 먼 곳에 있는 노드까지의 거리 찾기
distance는 루트에서 다른 노드까지의 거리를 나타내며,
-1이 아니면 해당 노드는 방문해서 distance를 구했다는 뜻
"""
distance = [-1] * (n+1)
rootToMaxNodeIndex= 0
# root index = 1
distance[1] = 0
dfs(1, 0)

rootToMaxNodeDistance= 0
for idx in range(1, n+1):
  if distance[idx] > rootToMaxNodeDistance:
    rootToMaxNodeDistance = distance[idx]
    rootToMaxNodeIndex = idx

"""
루트에서 가장 먼 노드 rootToMaxNodeIndex를 구했다면,
이 노드에서부터 가장 먼 거리에 있는 노드를 찾는다.
이 둘의 차이가 트리의 지름이 됨.
"""
distance = [-1] * (n+1)
distance[rootToMaxNodeIndex] = 0
dfs(rootToMaxNodeIndex, 0)

secondStepMaxNodeIndex = rootToMaxNodeIndex
secondStepMaxNodeDistance= 0
for idx in range(1, n+1):
  if distance[idx] > secondStepMaxNodeDistance:
    secondStepMaxNodeDistance = distance[idx]

treeDiameter = secondStepMaxNodeDistance
# root에서 가장 먼 노드와 그 노드에서부터 가장 먼 노드 사이의 거리
# 즉, 트리의 지름
print(treeDiameter)
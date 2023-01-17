# 1167 트리의 지름
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**4)

def dfs(cur_point, totalWeight):
  # 현재 노드와 간선으로 연결된 모든 노드 방문
  for point in graph[cur_point]:
    node, weight = point
    if distance[node] == -1: # 방문 안했다면
      distance[node] = totalWeight + weight
      dfs(node, distance[node])

# V= 트리의 정점 개수 (1~V)
V = int(input())
graph = [[] for _ in range(V+1)] # 번호가 1부터 시작니까 V+1개 생성
for _ in range(V):
  arr = list(map(int, input().split()))
  arr.pop() # 마지막 '-1' 제거
  idx = 1 # 간선으로 연결된 각 node의 start point를 잡아주기 위함.
  for _ in range(len(arr)//2):
    graph[arr[0]].append( [arr[idx], arr[idx+1]] )
    idx+=2

distance = [-1] * (V+1) # distance는 거리를 나타내기도 하며, visted check용도로도 쓰임.
rootToMaxNodeIndex= 0
# root index = 1
distance[1] = 0
dfs(1, 0)

rootToMaxNodeDistance= 0
# 루트에서 가장 먼 노드 찾기
for idx in range(1, V+1):
  if distance[idx] > rootToMaxNodeDistance:
    rootToMaxNodeIndex = idx
    rootToMaxNodeDistance = distance[idx]

# '루트에서 가장 먼 노드'랑 이 노드에서 가장 먼 노드까지의 거리가 트리의 지름
distance = [-1] * (V+1)
distance[rootToMaxNodeIndex] = 0
dfs(rootToMaxNodeIndex, 0)

diameter = max(distance)
print(diameter)
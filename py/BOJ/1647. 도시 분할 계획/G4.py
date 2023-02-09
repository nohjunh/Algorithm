# 1647 도시 분할 계획
import sys
input = sys.stdin.readline

def find_parent(parent, node):
  if parent[node] != node:
    parent[node] = find_parent(parent, parent[node])
  return parent[node]

def union_parent(parent, a, b):
  aNode_P = find_parent(parent, a)
  bNode_P = find_parent(parent, b)
  if aNode_P < bNode_P:
    parent[bNode_P] = aNode_P
  else:
    parent[aNode_P] = bNode_P

# N= 집의 수, M= 길의 수
N, M = map(int, input().split())
parent = [0] * (N+1)

roads = []
roadCosts = []
resultCost = 0

for i in range(1, N+1):
  parent[i] = i

for _ in range(M):
  aHome, bHome, cost = map(int, input().split())
  roads.append((cost, aHome, bHome))

roads.sort()

for road in roads:
  cost, aHome, bHome = road
  if find_parent(parent, aHome) != find_parent(parent, bHome):
    union_parent(parent, aHome, bHome)
    roadCosts.append(cost)
    resultCost += cost

print(resultCost - max(roadCosts))

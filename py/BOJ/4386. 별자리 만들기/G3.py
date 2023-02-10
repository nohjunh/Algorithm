#4386 별자리 만들기
import sys, math
input = sys.stdin.readline

def find_parent(parent, pointIdx):
  if parent[pointIdx] != pointIdx:
    parent[pointIdx] = find_parent(parent, parent[pointIdx])
  return parent[pointIdx]
  
def union_parent(parent, aPoint, bPoint):
  a = find_parent(parent, aPoint)
  b = find_parent(parent, bPoint)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# n= 별의 개수
n = int(input())
points = []
temp = [list(map(float, input().split())) for _ in range(n)]
for i in range(n):
  for j in range(i+1, n):
    xDiff = temp[j][0] - temp[i][0]
    yDiff = temp[j][1] - temp[i][1]
    points.append((math.sqrt(xDiff**2 + yDiff**2), i+1, j+1))
points.sort()

parent = [0] * (n+1)
resultCost= 0

for i in range(1, n+1):
  parent[i] = i

for point in points:
  cost, aPoint, bPoint = point
  if find_parent(parent, aPoint) != find_parent(parent, bPoint):
    union_parent(parent, aPoint, bPoint)
    resultCost += cost

print(f'{resultCost:.2f}')
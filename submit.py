# 2170 선 긋기
from sys import stdin
input = stdin.readline

"""
1 2 3
  2 3 4 5
    3 4 5
          6 7
"""

pointSet= [list(map(int, input().split())) for _ in range(int(input()))]
pointSet.sort(key = lambda x:x[0])
tracePointX, tracePointY= pointSet[0]
result= 0

for idx in range(1, len(pointSet)):
  curPointX, curPointY = pointSet[idx]
  if tracePointY < curPointX:
    result += tracePointY-tracePointX
    tracePointX, tracePointY = pointSet[idx]
  else:
    tracePointY = tracePointY if tracePointY > curPointY else curPointY
result += tracePointY-tracePointX

print(result)

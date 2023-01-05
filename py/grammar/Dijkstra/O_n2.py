# 다익스트라 test
# basic O(n**2)

import numpy as np

INF= 1000000000
number=6

a= np.array([
  [0, 2, 5, 1, INF, INF],
  [2, 0, 3, 2, INF, INF],
  [5, 3, 0, 3, 1,5],
  [1, 2, 3, 0, 1, INF],
  [INF, INF, 1, 1, 0, 2],
  [INF, INF, 5, INF, 2, 0]
])

# 방문한 노드 v배열
v= [False for _ in range(number)]
# 노드 거리 d배열
d= [0 for _ in range(number)]

def getSmallIndex():
  min= INF
  index= 0
  for i in range(number):
    if (d[i] < min) and not v[i]:
      min = d[i]
      index = i
  return index

def dijkstra(start):
  for i in range(number):
    d[i] = a[start][i]

  v[start]= True

  for i in range(number-2):
    current= getSmallIndex()
    v[current]= True
    for j in range(number):
      if not v[j]:
        if d[current] + a[current][j] < d[j]:
          d[j] = d[current] + a[current][j]


dijkstra(0)
for i in d:
  print(i)
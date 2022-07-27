# 최소힙

import heapq
import sys

heap = []
count=0
N= int(sys.stdin.readline())
for i in range(N):
  test = int(sys.stdin.readline())
  if test!=0:
    count+=1
    heapq.heappush(heap, test)
  else:
    if count==0:
      print("0")
    else:
      print(heapq.heappop(heap))
      count-=1


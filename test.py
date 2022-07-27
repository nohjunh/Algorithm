# 최대힙

import heapq
import sys

heap = []
list = []
count=0
N= int(sys.stdin.readline())
for i in range(N):
  test = int(sys.stdin.readline())
  if test!=0:
    list.append(test)
    count+=1
    for value in list:
      # 여기서 - 붙여서 heappush 해주는게 최대힙에서 중요!
      heapq.heappush(heap, -test)
    list.clear()
  else:
    if count==0:
      print("0")
    else:
      # 여기서 -로 push해줬으니까 - 붙여서 pop 판단근거 만들기 중요!
      print(-heapq.heappop(heap))
      count-=1


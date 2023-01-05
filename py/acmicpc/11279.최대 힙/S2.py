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
      heapq.heappush(heap, -test)
    list.clear()
  else:
    if count==0:
      print("0")
    else:
      print(-heapq.heappop(heap))
      count-=1


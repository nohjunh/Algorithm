import sys
import heapq

N= int(input())
heap=[]

for _ in range(2):
    x= int(input().rstrip())
    if x!=0:
        # 힙에 넣을 때 절댓값과 기존 값을 묶어서 넣는다.
        heapq.heappush(heap, (abs(x), x))

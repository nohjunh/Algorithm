# 11286 절댓값 힙
import sys
import heapq
input= sys.stdin.readline

N= int(input())
heap=[]
for _ in range(N):
    x= int(input().rstrip())
    if x!=0:
        # 힙에 넣을 때 절댓값과 기존 값을 튜플형태로 묶어서 넣는다.
        heapq.heappush(heap, (abs(x), x))
    if x==0:
        if len(heap)!=0:
            # 실제 값은 튜플의 두번 째 자리에 저장되어 있으므로
            # [1]인덱싱으로 접근한다.
            print(heapq.heappop(heap)[1])
        else:
            print("0")
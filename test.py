# min heap

import heapq
# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  heap= []
  result= []
  #모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(heap, value)
  
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(heap)):
    result.append(heapq.heappop(heap))
  return result

result= heapsort([1,3,4,7,9,2,4,6,8,0])
print(result)
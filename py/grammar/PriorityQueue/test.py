#Priority queue

######## 1. Priority queue unordered list ver.
class UnorderedMinPQ:
  def __init__(self):
    self.pq= []
  def insert(self, key):
    self.pq.append(key)
  def delMin(self):
    minId, min = None, None
    for idx, item in enumerate(self. pq):
      if minId == None or item < min:
        minId, min = idx, item
    del self.pq[minId] #del 키워드를 통한 삭제
    return min # 최솟값 반환

# if __name__ == "__main__":
#   pq = UnorderedMinPQ()
#   pq.insert(3)
#   pq.insert(4)
#   min= pq.delMin()
#   print(min)

######### 2. Priority queue Heap ver. [ (example) 최대값만 남겨놓음 ]
from queue import PriorityQueue

def topM(input, m):
    pq = PriorityQueue()
    for i in input:
        pq.put(i)
        if pq.qsize() > m:
            pq.get()

    return [pq.get() for _ in range(m)]

if __name__ == "__main__":    
    print(topM([52,21,50,100,-24,-6,2,26,42,77,89,0,-44],4))
    print(topM([61,18,2,-100,-24,77],3))
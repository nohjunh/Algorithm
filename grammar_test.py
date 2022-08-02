import heapq

graph= {
    'A': 10000
}

graph['A']=20
heap= []

# 요소 첫번째 두번째는 pop할때 따로따로 받을 수 있다.
# 다음과 같이,

heapq.heappush(heap, [graph['A'], 'STart'])

first, second = heapq.heappop(heap)
print(first, second)
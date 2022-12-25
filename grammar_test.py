# 코딩테스트 Good Code #Part 3

# 1-1. 순열, 조합
"""
# for문 사용 ver nC_2
# 1 2 3 4
# 1 2 # 1 3 # 1 4 # 2 3 # 2 4 # 3 5
arr = list(map(int, input().split()))
for i in range(0, len(arr)):
  for j in range(i+1, len(arr)):
    print(arr[i], arr[j])

# itertools를 사용한 조합(combination)
from itertools import combinations
print(list(combinations( [1,2,3,4], 2 )))
"""

"""
# 1~N까지 자연수 중에서 가능한 조합 리스트 다 출력
from sys import stdin
from itertools import combinations
input = stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
print(list(combinations(arr, M)))
"""

# 1-3. 순열
"""
from itertools import permutations
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
print(list(permutations(arr, 2)))
"""

# 2-1. 빈도 계산
"""
# Counter는 dict클래스의 하위 클래스로, 리스트나 튜플에서
# 각 데이터가 등장한 횟수를 dict형식으로 리턴해줌.
from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt = Counter(colors)
print(cnt)
# 상위 2개의 결과만 원하면
# print(cnt.most_common(2))
"""
"""
from collections import Counter
arr = [int(input()) for _ in range(int(input()))]
val = Counter(arr).most_common()
print(val)
print(val[0])
print(val[0][0])
"""

# 3-1. 최소힙, 최대힙
"""
import heapq
# heapq의 default는 최소힙
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 8)
print(len(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
# 최대 힙은 입력값에 -1을 곱해서 heap에 넣어주면 가장 큰 값이 가장 작은 값이므로 root에 위치하게 된다.
# heap에서 pop할 때 다시 -1을 곱해주면 원본 값이 나올 것이다.
"""

# 4-1. deque
"""
from collections import deque
deq = deque()
deq = deque([i for i in range(1, 5)])
print(deq)
deq.appendleft(10)
print(deq)
deq.append(-10)
print(deq)
print(deq.pop())
print(deq.popleft())
print(len(deq))
print(list(deq))
# rotate (인자에 양수 -> 인자 수만큼 좌측 회전), (인자에 음수 -> 우측 회전)
print(list(deq))
deq.rotate(-1)
print(list(deq))
deq.rotate(1)
print(list(deq))
"""

# PriorityQueue
"""
from queue import PriorityQueue
que = PriorityQueue()
que.put(4)
que.put(10)
que.put(2)

for i in range(len(que.queue)):
  print(que.queue[i])
"""
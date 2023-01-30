# 13549 숨바꼭질 3
"""
순간이동이 0초이므로 우선순위가 가장 낮다.
순간이동이 deque에서 우선순위가 가장 높도록 설정해
순간이동에 의해 먼저 방문체크가 되도록 한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

def BFS(point):
  distance[point] = 0
  queue = deque()
  # 현재 위치, 초 (0초부터 시작)
  queue.append((point, 0))

  while queue:
    curPoint, count= queue.popleft()
    if curPoint == K:
      print(count)
      break
    # 순간이동은 0초 즉, 우선순위가 제일 높으므로 맨 앞에 넣어줌. 먼저 방문할 수 있도록
    if 2*curPoint < maxScope and distance[2*curPoint] == -1:
      distance[2*curPoint] = count
      queue.appendleft((2*curPoint, count))
    if curPoint-1 >= 0 and distance[curPoint-1] == -1:
      distance[curPoint-1] = count+1
      queue.append((curPoint-1, count+1))
    if curPoint+1 < maxScope and distance[curPoint+1] == -1:
      distance[curPoint+1] = count+1
      queue.append((curPoint+1, count+1))

maxScope = 100001
# 수빈이 위치, 동생 위치
N, K = map(int, input().split())
distance = [-1 for _ in range(maxScope)]

BFS(N)
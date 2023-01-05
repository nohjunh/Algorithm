from collections import deque
import queue
import sys
input = sys.stdin.readline

N=int(input())
que= deque()

for i in range(1, N+1):
    que.append(i)

while(len(que)!=1):
    que.popleft()
    que.append(que.popleft())

print(que[0])
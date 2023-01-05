import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
que= deque()
ans= []

for i in range(1, N+1):
  que.append(i)

while(len(que)!=0):
  for _ in range(K-1):
    que.append(que[0])
    que.popleft()
  ans.append(que.popleft())

print("<", end='')
print(*ans, sep=', ',end='')
print(">")

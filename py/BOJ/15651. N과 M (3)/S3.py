# 15651. N과 M (3)
import sys
input = sys.stdin.readline

def dfs():
  if len(temp) == M:
    print(*temp)
    return
  for i in range(1, N+1):
    temp.append(i)
    dfs()
    temp.pop()

N, M = map(int, input().split())
temp = []

dfs()
# 2565 전깃줄
from sys import stdin
input = stdin.readline

N= int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
DP = [0 for _ in range(N+1)]
arr.sort(key = lambda x: x[0])

for i in range(N):
  for j in range(i):
    if arr[i][1] > arr[j][1] and DP[i] < DP[j]:
      DP[i] = DP[j]
  DP[i] += 1
print(N-max(DP))
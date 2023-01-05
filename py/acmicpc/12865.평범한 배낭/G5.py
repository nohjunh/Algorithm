# 12865 평범한 배낭
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
items= [[0,0]]
for i in range(N):
  items.append(list(map(int, input().split())))
DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
  W, V = items[i]
  for j in range(1, K+1):
    if j < W:
      DP[i][j] = DP[i-1][j]
    else:
      DP[i][j] = max(DP[i-1][j], DP[i-1][j-W]+V)

print(max(DP[N]))
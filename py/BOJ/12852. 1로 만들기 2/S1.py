# 12852 1로 만들기 2
import sys
input = sys.stdin.readline

N = int(input())
DP = [0] * (N+1)
store = [[1] for _ in range(N+1)]

for i in range(2, N+1):
  DP[i] = DP[i-1] + 1
  store[i] = store[i-1] + [i]
  if i % 2 == 0 and DP[i // 2] + 1 < DP[i]:
    DP[i] = DP[i // 2] + 1
    store[i] = store[i // 2] + [i]
  if i % 3 == 0 and DP[i // 3] + 1 < DP[i]:
    DP[i] = DP[i // 3] + 1
    store[i] = store[i // 3] + [i]
print(DP[N])
print(*reversed(store[N]))

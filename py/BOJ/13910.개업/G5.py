import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
wok = list(map(int, input().split()))

combi = list(combinations(wok, 2))
k = []
for i in combi:
    k.append(sum(i))
DP = [1e9] * (N+1)
for i in wok:
    k.append(i)
k = set(k)
for i in k:
    if i <= N:
        DP[i] = 1
for cnt in range(N+1):
    for i in k:
        if i <= cnt:
            DP[cnt] = min(DP[cnt], DP[cnt-i]+1)

print(DP[N])

#2156 포도주 시식
import sys
input= sys.stdin.readline

n= int(input())
wine = []
DP = []
for _ in range(n):
  wine.append(int(input()))

DP.append(wine[0])
if n > 1: # index-error 방지
  DP.append(wine[0]+wine[1])
if n > 2:
  DP.append(max(wine[0]+wine[2], wine[1]+wine[2], DP[1]))
for i in range(3, n):
  DP.append(max(DP[i-2]+wine[i], DP[i-3]+wine[i-1]+wine[i], DP[i-1]))

print(max(DP))

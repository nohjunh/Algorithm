# 11053 가장 긴 증가하는 부분 수열
from sys import stdin
input = stdin.readline

N= int(input())
arr= list(map(int, input().split()))
DP = [1 for _ in range(N)]

for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      DP[i]= max(DP[i], DP[j]+1)
print(max(DP))
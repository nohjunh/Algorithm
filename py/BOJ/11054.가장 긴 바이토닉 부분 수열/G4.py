# 11054 가장 긴 바이토닉 부분 수열
from sys import stdin
input = stdin.readline

N= int(input())
arr = list(map(int, input().split()))
lenDpForWard = [1 for _ in range(N)]
lenDpBackWard = [1 for _ in range(N)]
totalDP=[1 for _ in range(N)]

for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      lenDpForWard[i]= max(lenDpForWard[i], lenDpForWard[j]+1)

arr.reverse()

for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      lenDpBackWard[i]= max(lenDpBackWard[i], lenDpBackWard[j]+1)

lenDpBackWard.reverse()

for i in range(N):
  totalDP[i]= lenDpForWard[i]+lenDpBackWard[i]

print(max(totalDP)-1)
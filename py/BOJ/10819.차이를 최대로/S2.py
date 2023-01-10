# 10819 차이를 최대로
from sys import stdin
input = stdin.readline

def dfs(depth, list):
  global maxValue
  if depth == N:
    sum=0
    for i in range(1, N):
      sum+= abs(list[i-1] - list[i])
    maxValue = max(maxValue, sum)
    return
  for i in range(N):
    if not vistied[i]:
      list.append(arr[i])
      vistied[i]=True
      dfs(depth+1, list)
      list.pop()
      vistied[i]=False

N= int(input())
arr = list(map(int, input().split()))
maxValue = -1e9
vistied= [False]*(N)

dfs(0, [])
print(maxValue)
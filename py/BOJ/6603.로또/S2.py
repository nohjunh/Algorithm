#6603 로또
from sys import stdin
input = stdin.readline

def dfs(idx, result):
  if len(result) == 6:
    print(*result)
    return
  if idx >= k:
    return
  result.append(arr[idx])
  dfs(idx+1, result)
  result.remove(arr[idx])
  dfs(idx+1, result)

while True:
  k, *arr = map(int, input().split())
  if k == 0:
    break
  result= []
  dfs(0, result)
  print()
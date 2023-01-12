#16198 에너지 모으기
from sys import stdin
input = stdin.readline

def dfs(arr, energy):
  global maxValue
  if len(arr) == 2:
    maxValue = max(maxValue, energy)
    return
    
  for idx in range(1, len(arr)-1):
    energy_temp = arr[idx-1] * arr[idx+1]
    temp = arr[idx]
    energy += energy_temp
    del arr[idx]
    dfs(arr, energy)
    arr.insert(idx, temp)
    energy -= energy_temp

N= int(input())
arr = list(map(int, input().split()))
maxValue = -1e9

dfs(arr, 0)
print(maxValue)
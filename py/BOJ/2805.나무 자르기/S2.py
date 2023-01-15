#2805 나무 자르기
# 이진탐색 바이너리서치 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree= list(map(int, input().split()))

minValue, maxValue = 1, max(tree)

while minValue <= maxValue:
  midValue = (minValue+maxValue) // 2

  cutSum = 0
  for i in tree:
    if i >= midValue:
      cutSum += (i-midValue)
  
  if cutSum >= M:
    minValue = midValue + 1
  else:
    maxValue = midValue - 1
print(maxValue)
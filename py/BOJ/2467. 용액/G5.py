# 2467 용액
import sys
input = sys.stdin.readline
INF = sys.maxsize

# N= 전체 용액의 수
N= int(input())
solution = list(map(int, input().split()))

left, right = 0, N-1
twoPick = (0, 0)
preValue = INF

while left < right:
  twoSum = solution[left] + solution[right]
  if abs(twoSum) == 0:
    twoPick = (solution[left], solution[right])
    break
  if abs(twoSum) < preValue:
    preValue = abs(twoSum)
    twoPick = (solution[left], solution[right])
  if twoSum < 0:
    left += 1
  else:
    right -= 1

print(*twoPick)
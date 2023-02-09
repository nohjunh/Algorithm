# 2473 세 용액
import sys
input = sys.stdin.readline
INF = sys.maxsize

# N= 전체 용액의 수
N= int(input())
solution = list(map(int, input().split()))
solution.sort()
threePick = (0, 0, 0)
preValue = INF

"""
투포인터를 돌리는데, 세 용액을 선택해야 하므로 for문으로 하나의 용액을
고정시켜놓아야 함.
"""
for fixedValue in range(N):
  left, right = 0, N-1
  while left < right:
    if fixedValue == left:
      left += 1
      continue
    if fixedValue == right:
      right -= 1
      continue
    sum = solution[fixedValue] + solution[left] + solution[right]
    if sum == 0:
      threePick = (solution[fixedValue], solution[left], solution[right])
      print(*threePick)
      exit()
    if abs(sum) < preValue:
      preValue = abs(sum)
      threePick = (solution[fixedValue], solution[left], solution[right])
    if sum < 0:
      left += 1
    else:
      right -= 1
print(*threePick)
    
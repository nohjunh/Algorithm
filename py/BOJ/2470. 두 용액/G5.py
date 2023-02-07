# 2470 두 용액
import sys
input = sys.stdin.readline

# N = 전체 용액의 수
N= int(input())
solution = list(map(int, input().split()))

solution.sort()
left, right = 0, N-1
result = sys.maxsize
twoPick = (0,0)

while left < right:
  sum = solution[left] + solution[right]
  if sum == 0:
    twoPick = (solution[left], solution[right])
    break
  if abs(sum) < result:
    result= abs(sum)
    twoPick = (solution[left], solution[right])
  if sum < 0:
    left += 1
  else:
    right -= 1

print(*twoPick)
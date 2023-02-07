# 3273 두 수의 합
import sys
input = sys.stdin.readline

# n= 수열의 수, x= 찾고자 하는 합
n= int(input())
arr= list(map(int, input().split()))
x= int(input())
count= 0
end= 0

arr.sort()
left, right = 0, n-1
while left < right:
  twoNumSum = arr[left] + arr[right]
  if twoNumSum == x:
    count += 1
    left += 1
  elif twoNumSum < x:
    left +=1
  else:
    right -= 1

print(count)
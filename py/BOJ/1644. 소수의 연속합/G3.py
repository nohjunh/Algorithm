#1644. 소수의 연속합
import sys
input = sys.stdin.readline

def isPrime(number):  #에라토스테네스의 체
  i= number
  sqrt = int(i**(1/2))
  for j in range(2, sqrt+1): # 2부터 제곱근까지 나눠봄
    if i % j == 0:
      return False
  return True

# N= 자연수
N= int(input())
interval_sum = 0
end = 0
count = 0
primeNums = []
for i in range(2, N+1):
  check = isPrime(i)
  if check == True:
    primeNums.append(i)
    
for start in range(len(primeNums)):
  while interval_sum < N and end < len(primeNums):
    interval_sum += primeNums[end]
    end += 1    
  if interval_sum == N:
    count += 1
  interval_sum -= primeNums[start]

print(count)
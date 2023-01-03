# 1929 소수 구하기
# 에라토스테네스의 체
"""
만약, 12가 primeNumber인지 확인하고 싶다면
12의 약수 : 1 2 3 4 6 12

1 * 12
2 * 6
3 * 4
--대칭--
4 * 3
6 * 2
12 * 1
이므로 2,3 만 12%2,3==0 인지 여부 판단해주면 됨.
2,3 에서 0이 나온다면 4,6에서도 마찬가지로 0이 나올 것
"""

from sys import stdin
input = stdin.readline

def isPrime(number):
  i= number
  sqrt = int(i**(1/2))
  for j in range(2, sqrt+1): # 2부터 제곱근까지 나눠봄
    if i % j == 0:
      return False
  return True

M, N = map(int, input().split())
for i in range(M, N+1): # M부터 N까지
  if i==1:
    continue
  else:
    if isPrime(i):
      print(i)
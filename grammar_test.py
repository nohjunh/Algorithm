import sys
input= sys.stdin.readline

def facto(num):
  if num<=1:
    return 1
  else:
    return num*facto(num-1)

# 이항계수: n!/(n-k)!k!
N, K= map(int, input().split())
print(int(facto(N)/(facto(N-K)*facto(K))))
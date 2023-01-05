import math
import sys

T= int(sys.stdin.readline())
for _ in range(T):
  H, W, N= map(int, sys.stdin.readline().split())
  floor= N%H ## 층 수
  count= math.ceil(N/H) ## 몇 번째 호수
  if floor==0:
    floor= H
  print(floor*100+count)
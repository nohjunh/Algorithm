# 1912 연속합
import sys
input= sys.stdin.readline

n= int(input())
num_list=list(map(int,input().rstrip().split()))

for i in range(1, n):
  # i=1일때, max(-4,6) 6이 맥스!
  # i=2일때, max(3, 6+3) 9가 맥스!
  num_list[i]= max(num_list[i], num_list[i-1]+num_list[i])

print(max(num_list))
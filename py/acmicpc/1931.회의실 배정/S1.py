# 1931 회의실 배정 -> 그리디
import sys
from collections import deque
input= sys.stdin.readline

# 회의의 수
N= int(input())
test_list=[]
for i in range(N):
  start, end= map(int, input().split())
  test_list.append((start, end))

test_list=sorted(test_list,key=lambda x:x[0]) # 시작시간으로 우선 정렬
test_list=sorted(test_list,key=lambda x:x[1]) # 끝나는 시간으로  정렬

last_time=0
count=0
for start, end in test_list:
  if last_time<=start:
    count+=1
    last_time=end
  else:
    continue
print(count)
import sys
from collections import deque
input= sys.stdin.readline

# 정수 A
# 목표 정수 B
A, B= map(int, (input().rstrip().split()))

def BFS_with_adj_list(root):
  queue= deque([(root, 1)])
  while queue:
      num, count = queue.popleft()
      if num==B:
        print(count)
        exit()
      if num<=B:
        queue.append( (num*2, count+1) )
        queue.append( (int(str(num)+str(1)), count+1) )
      else:
        continue
BFS_with_adj_list(A)
print("-1")
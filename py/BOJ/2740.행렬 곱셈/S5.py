import math
import sys

N, M= map(int, sys.stdin.readline().split())
A_list= []
for i in range(N):
  A_list.append(list(map(int, sys.stdin.readline().split())))

N, M= map(int, sys.stdin.readline().split())
B_list= []
for i in range(N):
  B_list.append(list(map(int, sys.stdin.readline().split())))

All_list= []

for i in range(len(A_list)):
  for j in range(M):
    test=0
    for k in range(len(A_list[i])):
      test+= A_list[i][k]*B_list[k][j]
    All_list.append(test)

def list_chuck(arr, n):
    return [arr[i: i + n] for i in range(0, len(arr), n)]

list_chunked= list_chuck(All_list, 3)
for i in list_chunked:
  print(*i)
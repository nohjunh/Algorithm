# 9251 LCS
# ref) https://youtu.be/z8KVLz9BFIo
import sys, pprint
input = sys.stdin.readline

A= input().rstrip()
B= input().rstrip()

table = [ [0]*(len(B)+1) for _ in range(len(A)+1) ]

for i in range(1, len(A)+1):
  for j in range(1, len(B)+1):
    if A[i-1] == B[j-1]:
      table[i][j] = table[i-1][j-1] + 1
    else:
      table[i][j] = max(table[i-1][j], table[i][j-1])

print(table[-1][-1])
#2295 세 수의 합
import sys
input = sys.stdin.readline

N= int(input())
U = set()
for i in range(N):
  U.add(int(input()))

sumSet= set()
for i in U:
  for j in U:
    sumSet.add(i + j)

result = []
for i in U:
  for j in U:
    if (i-j) in sumSet:
      result.append(i)
      
print(max(result))

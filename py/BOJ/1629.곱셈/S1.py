import sys
A,B,C= map(int, sys.stdin.readline().split())

def solve(A,B):
  if B==1:
    return A%C
  temp= solve(A, B//2)

  if B%2==0:
    return temp*temp % C
  else:
    return temp*temp*A % C

print(solve(A,B))
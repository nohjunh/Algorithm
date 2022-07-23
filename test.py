"""
n=1 -> 1 1개
n=2 -> 00, 11 2개
n=3 -> 100 , 001, 111 3개
n=4 -> 0000, 0011, 1100, 1001, 1111 5개
n=5 -> 8개

DP[n]= DP[n-1] + DP[n-2]
"""

def solve(N):
  for i in range(3, N+1):
    DP[i]= (DP[i-1] + DP[i-2]) % 15746
  return DP[N]

N= int(input())
DP = [0 for _ in range(N+1)]
DP[1]=1
DP[2]=2
if N==1 or N==2:
  print(N%15746)
else:
  ans = solve(N)
  print(ans)
def solve(N):
  DP[1]=1
  DP[2]=2
  for i in range(3, N+1):
    DP[i]= (DP[i-1] + DP[i-2]) % 15746
  return DP[N]

N= int(input())
DP = [0 for _ in range(N+1)]
if N==1 or N==2:
  print(N%15746)
else:
  ans = solve(N)
  print(ans)
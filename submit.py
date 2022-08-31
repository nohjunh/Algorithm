# 9461 파도반수열
import sys
input= sys.stdin.readline

T=int(input().rstrip())
DP=[0 for _ in range(101)]
DP[0]=1
DP[1]=1
DP[2]=1
DP[3]=2
DP[4]=2
for i in range(5, 101):
  DP[i]= DP[i-1]+DP[i-5]
#DP[5]=DP[0]+DP[4] => 5-1 + 5-5
#DP[6]=DP[1]+DP[5] => 6-5 + 6-1
#DP[7]=DP[2]+DP[6] => 7-1 + 7-7
#DP[8]=DP[3]+DP[7] => 8-1 + 8-5 
for _ in range(T):
  N=int(input().rstrip())
  print(DP[N-1])
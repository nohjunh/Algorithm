# 9095
import sys
input= sys.stdin.readline

T= int(input())
DP=[0]*(11) #N의 크기는 11보다 작다.
DP[1]=1 
DP[2]=2
DP[3]=4
DP[4]=7
for i in range(5,11):
  DP[i]=DP[i-1]+DP[i-2]+DP[i-3]
for i in range(T):
  N=int(input())
  print(DP[N])    


  
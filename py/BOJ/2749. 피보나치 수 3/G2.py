#2749. 피보나치 수 3
# ref) https://www.acmicpc.net/blog/view/28
"""
피사노 주기(Pisano Period)= 피보나치 수를 K로 나눈 나머지는 항상 주기를 가짐.
주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같음.
나누려는 수가 10^k이고 이때  k > 2 라면, 주기는 항상 15*10^(k-1)가 됨.
이 문제에서 M = 10^6 이기 때문에, 주기는 15*10^5 = 1500000
"""
import sys
input = sys.stdin.readline

n= int(input())
fibo = [0, 1]
mod = 1000000
P = 1500000
# 한 주기만 계산해 fibo배열에 넣으면 됨.
for i in range(2, P):
  fibo.append(fibo[i-1]+fibo[i-2])
  fibo[i] = fibo[i]%mod
print(fibo[n%P])

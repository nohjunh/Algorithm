n= int(input()) # bound number
DP = [0] * (n+1)
DP[0] = 1 
for i in range(1, n+1):
  k = 0
  for j in range(i-1, -1, -1): # k = 0부터 N-1까지 증가, j = N(=i)-1-k (k가 1씩 증가하는게 for문이 진행됨에 따라 1씩 감소시키는 것과 동일)
    DP[i] += DP[j] * DP[k]
    k += 1
    
print(DP)
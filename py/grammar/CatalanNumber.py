def catalanNumber(n):
    DP = [0] * (n+1)
    DP[0] = 1
    
    for i in range(1, n+1):
      for k in range(0, i):
        DP[i] += DP[i-1-k]*DP[k]
        
    return DP[n]
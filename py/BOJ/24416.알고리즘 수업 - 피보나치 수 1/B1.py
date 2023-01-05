def fib(n):
  if n==1 or n==2:
    global count_code1
    count_code1+=1
    return 1
  else:
    return fib(n-1) + fib(n-2)
  

def fibonacci(n):
  DP[1] = DP[2] = 1
  for i in range(3, n+1):
    global count_code2
    count_code2+=1
    if DP[i]==0:
      DP[i]= DP[i-1] + DP[i-2]
    else:
      return DP[i]
  return DP[n]

DP= [0]*100
n= int(input())
global count_code1
count_code1=0
global count_code2
count_code2=0
fib(n)
fibonacci(n)
print(count_code1, count_code2)


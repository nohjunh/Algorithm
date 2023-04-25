def isPrime(number):  #에라토스테네스의 체
  i = number
  sqrt = int(i**(1/2))
  for j in range(2, sqrt+1): # 2부터 제곱근까지 나눠봄
    if i % j == 0:
      return False
  return True

def findPrimes(number):
    prime = [True for _ in range(number+1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= number:
        if prime[p]:
            prime[p*p::p] = [False] * ((number- p * p) // p+1)            
        p += 1

    result = []
    for i in range(len(prime)):
        if prime[i]: result.append(i)
    return result
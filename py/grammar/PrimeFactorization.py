def primeFactorization(n):
  result = []
  while n % 2 == 0:
    n /= 2
    result.append(2)

  p = 3
  while p*p <= n:
    while n % p == 0:
      n /= p
      result.append(p)
    p += 2

  if n > 2: result.append(int(n))
  return result

print(primeFactorization(10))
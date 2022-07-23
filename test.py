A,B= map(int, input().split())

def gcd(x,y):
  while y!=0:
    x2=y
    y= x%y
    x=x2
  return x

def lcm(x,y):
  return x*y // gcd(x,y)

print(gcd(A,B))
print(lcm(A,B))
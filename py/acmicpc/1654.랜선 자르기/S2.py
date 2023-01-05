K, N = map(int, input().split())
code= [int(input()) for _ in range(K)]

start=1
end= max(code)

while start < end:
  mid= (start+end)//2 +1
  count= sum([ i//mid for i in code])
  if count >= N:
    start= mid
  else:
    end= mid-1
  
print(start)
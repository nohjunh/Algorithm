n = int(input())
count=0
while True:
    if n==1 or n==2:
        count=-1
        break
    if n==0:
        break
    if n % 5 == 0:
        n-=5
        count+=1
    else:
        n-=3
        count+=1

print(count)
N= int(input())
test_set= list(map(int, input().split()))

count=0
for i in test_set:
    sosu= True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            sosu= False
            break
    if sosu==True:
        count+=1


print(count)
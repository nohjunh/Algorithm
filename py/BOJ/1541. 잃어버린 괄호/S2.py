inputList = input().split('-')
sum = 0
#print(inputList)
for i in inputList[0].split('+'):
    sum += int(i)
for i in inputList[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)
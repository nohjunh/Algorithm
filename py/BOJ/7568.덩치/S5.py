test_count= int(input())
test_set=[]

for i in range(test_count):
    weight, height = map(int, input().split())
    test_set.append( (weight, height) )

for i in range(len(test_set)):
    count=1
    for j in range(len(test_set)):
        if test_set[i][0] < test_set[j][0] and test_set[i][1] < test_set[j][1]:
            count+=1
    print(count, end=" ")
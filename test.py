test_count= int(input())
test_set={}
test_rank=[]

for i in range(test_count):
    weight, height = map(int, input().split())
    test_set[weight]= height

for i in test_set.keys():
    count=1
    for weight,height in test_set.items():
        if i < weight and test_set[i] < height:
            count+=1

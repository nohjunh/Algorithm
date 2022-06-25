test_count= int(input())
test_set= list(map(int, input().split()))

test_set2= list(set(test_set))
test_set3= sorted(test_set2)

test_dic = {}
for i in range(len(test_set3)):
    test_dic[ test_set3[i] ]= i

for num in test_set:
    print(test_dic[num], end=' ')


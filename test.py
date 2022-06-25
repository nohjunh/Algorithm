test_count= int(input())
test_set={}
for _ in range(test_count):
    x=input()
    test_set[x]= len(x)

result = sorted(test_set.items())
result1 = sorted(result, key=lambda x: x[1])


for a in result1:
    print(a[0])

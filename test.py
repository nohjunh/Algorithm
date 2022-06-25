a,b = map(int, input().split())
test_list=list(map(int, input().split()))
temp = [0]
sum=0
for i in test_list:
    sum+=i
    temp.append(sum)

print(temp)
for i in range(b):
    _from, _to= map(int, input().split())
    print(temp[_to] - temp[_from-1])
import sys

a,b = map(int, sys.stdin.readline().split())
test_list=list(map(int, sys.stdin.readline().split()))
temp = [0]
sum=0
for i in test_list:
    sum+=i
    temp.append(sum)

for i in range(b):
    _from, _to= map(int, sys.stdin.readline().split())
    print(temp[_to] - temp[_from-1])
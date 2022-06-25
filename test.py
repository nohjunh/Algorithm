count, max = map(int, input().split())
test_input=list(map(int, input().split()))
test_set=[]
for i in range(count):
    for j in range(i+1, count):
        for k in range(j+1, count):
            sum=test_input[i]+test_input[j]+test_input[k]
            if sum>max:
                continue
            else:
                test_set.append(sum)

test_set.sort(reverse=True)
print(test_set[0])
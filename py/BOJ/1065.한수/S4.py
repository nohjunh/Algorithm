test_number= int(input())
count=0
for num in range(1, test_number+1):
    test_string = list(map(int, str(num)))
    if num <100:
        count+=1
    else:
        if (test_string[0]-test_string[1]) == (test_string[1]-test_string[2]):
            count+=1

print(count)
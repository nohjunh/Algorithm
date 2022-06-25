import string

test_input= list(input())

for i in string.ascii_lowercase:
    x= i not in test_input
    if x:
        print("-1", end=' ')
    else:
        print(test_input.index(i), end=' ')

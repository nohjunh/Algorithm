test_set= list(range(1,10001))

del_set= set()

for number in test_set:
    sum=number
    for digit in str(number):
        sum+= int(digit)
    if(sum<=10000):
        del_set.add(sum)

for element in del_set:
    test_set.remove(element)

for step in test_set:
    print(step)
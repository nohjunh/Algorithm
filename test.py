test_input= input()
test_set= set()

for i in range( len(test_input)):
    for j in range( i, len(test_input) ):
        test_case= test_input[i:j+1]
        test_set.add(test_case)

print(len(test_set))


test_input= int(input())
test_set=[]
for i in range(test_input):
    a,b = input().split()
    test=""
    for j in b:
        for k in range(int(a)):
           test+=j
    test_set.append(test)

for i in test_set:
    print(i)
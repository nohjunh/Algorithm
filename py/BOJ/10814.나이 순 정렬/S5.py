test_input= int(input())
test_list= []
for i in range(test_input):
    A,B = map(str, input().split())
    A= int(A)
    test_list.append([A,B])

test_list.sort(key=lambda x:x[0])

for i in range(test_input):
    print(test_list[i][0], test_list[i][1])
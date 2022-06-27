test_list= int(input())

str= "*"
for i in range(test_list):
    print(str.rjust(test_list))
    str+="*"
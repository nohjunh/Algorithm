test_input= input()
lower_input= test_input.lower()

count= [0 for i in range(26)]

for x in lower_input:
    count[ord(x)-97]+=1

sorted_count= sorted(count, reverse=True)
check_num= count.index(sorted_count[0])
if sorted_count[0]==sorted_count[1]:
    print("?")
else:
    print(chr(check_num+97).upper())
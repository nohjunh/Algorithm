N= int(input())
dead_num=666
count=0
while(1):
  if '666' in str(dead_num):
    count+=1
  if count==N:
    print(dead_num)
    break
  else:
    dead_num+=1
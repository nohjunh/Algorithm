N= int(input())

num= 1
while(True):
  sum_value=0
  sum_value= num + sum(map(int, str(num)))
  if sum_value == N:
    print(num)
    break
  elif num>=N:
    print("0")
    break
  else:
    num+=1
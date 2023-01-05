import sys

N=int(sys.stdin.readline())
solve_list=[]
count=0
for i in range(N):
  initial= list(map(str,sys.stdin.readline().split()))
  Comm= initial[0]
  if len(initial)==2:
    value= initial[1]
  if Comm=="push":
    solve_list.append(int(value))
    count+=1
  elif Comm=="pop":
    if count==0:
      print("-1")
    else:
      count-=1
      print(solve_list.pop())
  elif Comm=="size":
    print(len(solve_list))
  elif Comm=="empty":
    if count==0:
      print("1")
    else:
      print("0")
  elif Comm=="top":
    if count==0:
      print("-1")
    else:
      print(solve_list[count-1])
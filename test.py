while(1):
  num= int(input())
  num_list = list(str(num))
  if num==0:
    break

  end= len(str(num))
  if end==1:
    print("yes")
  mid= end//2

  for i in range(mid):
    if num_list[i] == num_list[end-1]:
      end-=1
      if i+1==mid:
        print("yes")
        break
    else:
      print("no")
      break

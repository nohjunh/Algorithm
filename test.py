while(1):
    a = list(map(int, input().split()))
    max_value= max(a)
    if max_value==0:
        break
    a.remove(max_value)
    if (a[0]**2+a[1]**2) != max_value**2:
      print("wrong")
    else:
      print("right")

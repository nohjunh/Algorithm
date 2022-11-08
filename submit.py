def angle_Cal(points, p_Value): # 점 p로부터 반시계방향으로 거쳐가는 차례로 포함
  gradient_Set=[]
  for i in points:
    if i==p_Value:
      continue
    try:
      gradient= (i[1]-p_Value[1])/(i[0]-p_Value[0])
      ##### 0.0이 -가 나오는데 결국 같으므로 통일 시키기 위함.
      if gradient== -0.0:
        gradient=0.0
    except:
      gradient= float('inf')
    gradient_Set.append(gradient)
  return gradient_Set

def collinearPoints(points):
  ans=[]
  points= sorted(points, key=lambda p:(p[0],p[1]))
  gradient_collection=[]
  for i in points:
    gradient_Set= angle_Cal(points, i)
    counter = {}
    for value in gradient_Set:
      if value in counter:
          counter[value] += 1
      else:
          counter[value] = 1
    for key, value in counter.items(): # key=기울기, value= 그 기울기가 몇 개가 있는지
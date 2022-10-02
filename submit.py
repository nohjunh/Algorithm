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
      if value>=3:
        if (key,i[0],i[1]) in gradient_collection:
          continue
        else:
          index=0 # 마지막 요소의 인덱스값을 저장하기 위함.
          for j in enumerate(gradient_Set):
            if j[1]==key:
              index= j[0]
              gradient_collection.append((key, points[index+1][0],points[index+1][1]))
          ans.append((i[0],i[1], points[index+1][0],points[index+1][1]))
  return ans

if __name__ == "__main__":
  print(collinearPoints([(0,0), (3,1), (2,3), (4,4), (6,6), (7,7), (9,9)]))
  print(collinearPoints([(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]))
  print(collinearPoints([(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]))
  print(collinearPoints([(1,1), (2,2), (3,3), (4,4), (2,0), (3,-1), (4,-2), (0,1), (-1,1), (-2,1), (-3,1), (2,1), (3,1), (4,1), (5,1)]))
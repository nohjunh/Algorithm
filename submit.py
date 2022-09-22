import math

def ccw(i, j, k):
  area2= (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
  if area2 > 0:
    return True # 반시계방향 turn
  else:
    return False # 시계방향 turn

def get_P_Points(testPoints):
  testPoints= sorted(testPoints, key = lambda p: (p[1],-p[0])) # y값 기준 오름차순(y값이 제일 작은 값 찾음), x값 기준 내림차순 (x값이 제일 큰 값 찾음)
  return (testPoints[0][0], testPoints[0][1])  ## max_X_Value= testPoints[0][0], small_Y_Value= testPoints[0][1]

def angle_Cal(points, p_Value): # 점 p로부터 반시계방향으로 거쳐가는 차례로 포함
  points= sorted(points, key= lambda x:x[1]) #########중요######### -> 같은 각도일때 탐색 순서를 맞춰주기 위함.
  angleOrder=[]
  radian_Set=[]
  j=0
  for i in points:
    if i==p_Value:
      j+=1
      continue
    radian= math.atan2(i[1]-p_Value[1], i[0]-p_Value[0])
    #degree= radian*180 / math.pi
    radian_Set.append((j, radian))
    j+=1
  radian_Set= sorted(radian_Set, key=lambda x:x[1])
  for i in radian_Set:
    angleOrder.append(points[i[0]])
  return angleOrder

def grahamScan(points):
  p_Value= (get_P_Points(points))
  hull=[]
  hull.append(p_Value)
  angleOrder= angle_Cal(points, p_Value)
  angleOrder.append(p_Value) # 마지막 p_Value랑 연결해서 판단하게 하기위함
  for k in angleOrder:
    while len(hull) >=2:
      # stack기능이라고 생각해야되므로 append시 맨 뒤에 붙는거 고려.
      # 맨 뒤에서부터 한 두 개씩 가져온다.
      i,j = hull[-2], hull[-1] # [-1]: first, [-2]: second
      if ccw(i,j,k): 
        break # true이면 second값 hull에 그대로 있으면 됨.
      hull.pop() # false면 pop해서 second값 빼줌
    hull.append(k)
  hull.pop(-1) # 마지막 하나 추가한 p_Value가 hull에 들어가기에 빼줌(중복값)
  return hull


if __name__ == "__main__":
  # 백준 test_case
   hull=[]
   N=int(input())
   for i in range(N):
     a,b=map(int,input().split())
     hull.append((a,b))
   hull= grahamScan(hull)
   print(len(hull))
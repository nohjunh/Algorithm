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
      i, j = hull[-2], hull[-1] # [-1]: 맨 뒤 기준 first가 j에 들어간다., [-2]: 맨 뒤 기준 second가 i에 들어간다.
      if ccw(i,j,k):
        break # true이면 convex라는 뜻이므로 second값 hull에 그대로 있으면 되고, k값 hull에 push해주면 됨.
      hull.pop() # false면 concave라는 뜻이므로 pop해서 second값(즉, j값) 빼줌
    hull.append(k)
  hull.pop(-1) # 마지막 하나 추가한 p_Value가 hull에 들어가기에 빼줌(중복값)
  return hull
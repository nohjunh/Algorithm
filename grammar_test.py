def ccw(i, j, k):
  area2= (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
  if area2 > 0:
    return True # 반시계방향 turn
  else:
    return False # 시계방향 turn

# 2239 스도쿠
import sys
input = sys.stdin.readline

def row_valid(nx, num):
  for i in range(9):
    if num == sdoku[nx][i]:
      return False
  return True    

def col_valid(ny, num):
  for i in range(9):
    if num == sdoku[i][ny]:
      return False
  return True 
  
def square_valid(nx, ny, num):
  # ex) (5,3) 이면 5//3*3= 3이므로, xSquare범위는 3,4,5, 3//3*3 = 3이므로, ySquare범위도 3,4,5 즉 5,3은 (3,3)~(5,5) 네모안에 있음.
  x_square = (nx // 3)*3 
  y_square = (ny // 3)*3
  for i in range(3):
    for j in range(3):
      if num == sdoku[x_square+i][y_square+j]:
        return False
  return True
  
def DFS(depth): # depth는 제로포인트 갯수만큼 진행해야 함.
  if depth == len(zeroPoints):
    for i in range(9):
      print(''.join(map(str, sdoku[i])))
    exit()
  nx, ny = zeroPoints[depth]
  for num in range(1, 10): # 1~9 까지
    if col_valid(ny, num) and row_valid(nx, num) and square_valid(nx, ny, num):
      sdoku[nx][ny] = num
      DFS(depth+1)
      sdoku[nx][ny] = 0

sdoku = [list(map(int, input().rstrip())) for _ in range(9)]
zeroPoints= []
for i in range(9):
  for j in range(9):
    if sdoku[i][j] == 0:
      zeroPoints.append((i, j))

DFS(0)
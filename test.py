#https://leedakyeong.tistory.com/entry/Python-2-dimension-list
#https://computer-science-student.tistory.com/313
#파이썬에서 2차원 이상의 배열 생성초기화 시 주의해야할 점.

DP = [[[0]*51 for _ in range(51)]*51 for _ in range(51)] #3차원 배열

def w(a,b,c):
  if a<=0 or b<=0 or c<=0:
    return 1
  if a>20 or b>20 or c>20:
    if DP[a][b][c]!=0:
      return DP[a][b][c]
    return w(20,20,20)
  if a<b<c:
    if DP[a][b][c]!=0:
      return DP[a][b][c]
    else:
      DP[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
      return DP[a][b][c]
  else:
    if DP[a][b][c]!=0:
      return DP[a][b][c]
    DP[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return DP[a][b][c]


while(1):
  a,b,c= map(int, input().split())
  if a==-1 and b==-1 and c==-1:
    break
  print("w({}, {}, {}) =".format(a,b,c),w(a,b,c))
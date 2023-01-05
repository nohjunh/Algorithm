# 1074 Z
import sys
input= sys.stdin.readline
# r행 c열
N, r, c= map(int, input().split())

# 2^N X 2^N => Z모양 탐색
# N=2 => 4X4 2차원 배열 -> 2X2로 4등분
count=0
def solve(N, x, y): #행렬
  global count
  if x==r and y==c:
    print(round(count))
    exit()
  if N==1: # N=1이면 => 2X2 배열이고 조건에 맞지 않다면 그 분면은 지나치는거니 +1씩
    count+=1
    return
  # N=3이면 -> 8X8배열이고 -> 8/2이면->4 => 2X2배열 4개 -> x,y범위인 0~1 까지 중 r,c 없으면 그 배열 크기만큼 +해줌
  # N=4이면 -> 16X16배열이고 -> 16/2이면-> 8 => 4X4배열 4개-> x,y범위인 0~4까지 중 r,c 없으면 그 배열 크기만큼 +해줌
  if not (x<= r <x+N and y<= c <y+N):
    count += N*N
    return
  solve(N/2, x, y) # 2사분면
  solve(N/2, x, y+N/2) # x=행 , y=열이므로 이게 1사분면 가리킴.
  solve(N/2, x+N/2, y) # 3사분면
  solve(N/2, x+N/2, y+N/2) # 4사분면
    
solve(2**N,0,0) # N=2 -> 4X4

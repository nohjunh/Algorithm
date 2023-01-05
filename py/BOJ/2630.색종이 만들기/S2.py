def solve(x, y, N):
  # color 0= 흰, 1= 파
  global paper
  color = paper[x][y]
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != paper[i][j]:
        solve(x, y, N//2)
        solve(x+N//2, y, N//2)
        solve(x, y+N//2, N//2)
        solve(x+N//2, y+N//2, N//2)
        return
  if color == 0:
    global count_0
    count_0+=1
  else:
    global count_1
    count_1+=1 
  

N= int(input())
global paper
paper = []
global count_0, count_1
count_0=0
count_1=0
for _ in range(N):
  paper.append(list(map(int, input().split())))

solve(0,0,N)
print(count_0)
print(count_1)
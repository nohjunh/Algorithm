import sys
input= sys.stdin.readline

N= int(input())
data= []
for _ in range(N):
  a= list(map(int, input().split()))
  data.append(a)

for i in range(1, N):
  for j in range(len(data[i])):
    if j==0:
      data[i][j]= data[i][j]+ data[i-1][j]
    elif j==len(data[i])-1:
      data[i][j]= data[i][j]+ data[i-1][j-1]
    else:
      data[i][j] = max(data[i-1][j], data[i-1][j-1]) + data[i][j]
print(max(data[N-1]))
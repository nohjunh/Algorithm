n= int(input())
DP = []
for i in range(n):
  DP.append(list(map(int,input().split())))

row_element_count=2

for i in range(1,n):
  for num in range(row_element_count):
    if num==0:
      DP[i][num]= DP[i][num] + DP[i-1][num]
    elif i==num:
      DP[i][num]= DP[i][num] + DP[i-1][num-1]
    else:
      DP[i][num]= max(DP[i-1][num-1], DP[i-1][num])+DP[i][num]
  row_element_count+=1

print(max(DP[n-1]))

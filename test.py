import sys
input= sys.stdin.readline

T= int(input())
for _ in range(T):
  n= int(input())
  test_case=[]
  for i in range(2):
    test_case.append(list(map(int, input().split())))
  for j in range(1, n):
    if j==1:
      test_case[0][j] += test_case[1][j-1]
      test_case[1][j] += test_case[0][j-1]
    else:
      test_case[0][j]+=max(test_case[1][j-1], test_case[1][j-2])
      test_case[1][j]+=max(test_case[0][j-1], test_case[0][j-2])
  print(max(test_case[0][n-1], test_case[1][n-1]))
      

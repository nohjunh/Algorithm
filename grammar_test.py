def test(i, j):
  print(i,j)


N=4
for i in range(N):
  for j in range(N):
    print("True")
    test(i+1,j+1)
    print("False")
# 11444. 피보나치 수 6
# ref) https://www.acmicpc.net/blog/view/28
# ref) https://kimjerry.tistory.com/7
import sys
input = sys.stdin.readline

# 행렬 곱
def multi(matrix1, matrix2):
  temp = [[0]*2 for _ in range(2)]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        # a b = c -> c11 = a11*b11 + a12*b21
        temp[i][j] = temp[i][j] + (matrix1[i][k]*matrix2[k][j])
      temp[i][j] = temp[i][j] % 1000000007
  return temp 

#제곱을 구하기 위한 분할정복
def power(matrix, n):
  if n == 1:
    return matrix
  else:
    temp = power(matrix, n//2)
    if n % 2==0: # 짝수라면
      return multi(temp, temp)
    else: # 홀수라면
      """
          (3)      (2) 
        1 1  =   1 1   1 1
        1 0      1 0   1 0
      """
      return multi( multi(temp, temp), matrix )

N= int(input())
matrix = [[1,1], [1,0]]
print(power(matrix, N)[0][1])
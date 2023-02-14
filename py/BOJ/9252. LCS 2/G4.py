#9252 LCS 2
# ref) https://youtu.be/z8KVLz9BFIo

import sys, pprint
input = sys.stdin.readline

# 1 = 대각선, 2 = 왼쪽, 3 = 위

def LCS(input1, input2):  
  for i in range(1, len(input1)+1):
    for j in range(1, len(input2)+1):
      if input1[i-1] == input2[j-1]:
        DP[i][j] = DP[i-1][j-1] + 1
        BackT[i][j] = 1
      else:
        DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        BackT[i][j] = 3 if DP[i-1][j] > DP[i][j-1] else 2 
  return DP[-1][-1]
  
def getString():
  iPoint = len(input1)
  jPoint = len(input2)
  temp = -1
  answer = ""
  while temp!=0:
    if BackT[iPoint][jPoint] == 1:
      temp = BackT[iPoint-1][jPoint-1]
      answer += input1[iPoint-1] # 테이블은 index 0을 제외했지만 input데이터는 index 0부터 시작
      iPoint = iPoint-1
      jPoint = jPoint-1
    elif BackT[iPoint][jPoint] == 2:
      temp = BackT[iPoint][jPoint-1]
      jPoint = jPoint-1
    else:
      temp = BackT[iPoint-1][jPoint]
      iPoint = iPoint-1
  return answer
      
input1 = input().rstrip()
input2 = input().rstrip()

DP = [[0]*(len(input2)+1) for _ in range(len(input1)+1)]
BackT = [[0]*(len(input2)+1) for _ in range(len(input1)+1)]
  
print(LCS(input1, input2))
print(getString()[::-1])
# 11660. 구간 합 구하기 5
"""
누적합 그래프를 만들고 계산
ㅋㅁㅌ
ㅁㅅㅁ
ㅎㅁㅈ  
 ㅅ 부터 ㅈ 까지 구한다고 하면
 
 [ ㅈ까지의 누적합 - ㅌ까지의 누적합 - ㅎ까지의 누적합 + ㅋ까지의 누적합 ]
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

accArr = [[0]*(N+1) for _ in range(N+1)]
# 1행 1열은 구현의 편리함을 위해 사용하지 않음.
for i in range(1, N+1):
  for j in range(1, N+1):
    accArr[i][j] = accArr[i-1][j] + accArr[i][j-1] - accArr[i-1][j-1] + arr[i-1][j-1]

for i in range(M):
  x1, y1, x2, y2 = map(int, input().split())

  print(accArr[x2][y2] - accArr[x2][y1-1] - accArr[x1-1][y2] + (accArr[x1-1][y1-1]))
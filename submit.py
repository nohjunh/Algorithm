#2579 계단오르기
#https://daimhada.tistory.com/181
#이 tistory에 문제 접근 정리가 잘되어있음
import sys
input= sys.stdin.readline
# 계단의 갯수
N=int(input())
# 계단 점수 배열
score=[]
# 유효한 계단 점수의 인덱스를 1번부터 시작하기 위해 그냥 0번째 인덱스에 0을 넣음 (i-3에서 i가 3이되서 i=0이 되면 계단 출발 전의 범위고 0의 값이니까 0의 값은 최종값에 영향이 없게 됨.)
score.append(0)
for _ in range(N):
  score.append(int(input().rstrip()))

# 해당 번째 계단을 밟았을때의 최댓값 DPlist
DP_list=[0 for _ in range(N+1)]
if N==1:
  print(score[1])
else:
  DP_list[1]= score[1]
  DP_list[2]= score[1] + score[2]
  for i in range(3, N+1):
    DP_list[i]= max(score[i]+score[i-1]+DP_list[i-3], score[i]+DP_list[i-2])
  print(DP_list[N])
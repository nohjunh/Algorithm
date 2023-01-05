# 2579 RGB거리
import sys
input= sys.stdin.readline
# 집의 수
N=int(input())
DP_list=[]
# 0번 인덱스는 쓰레기값을 넣어서 유효한 범위를 1번 인덱스부터 하기 위함.
DP_list.append([0,0,0])
# 집을 칠하는 비용
for i in range(N):
  DP_list.append(list(map(int,input().rstrip().split())))

# DP리스트 갱신
for i in range(2, N+1):
  # 0번이면 빨강 => i번째 집을 빨강색으로 칠했을때 최솟값
  DP_list[i][0]=min(DP_list[i-1][1], DP_list[i-1][2])+ DP_list[i][0]
  DP_list[i][1]=min(DP_list[i-1][0], DP_list[i-1][2])+ DP_list[i][1]
  DP_list[i][2]=min(DP_list[i-1][0], DP_list[i-1][1])+ DP_list[i][2]

print(min(DP_list[N]))
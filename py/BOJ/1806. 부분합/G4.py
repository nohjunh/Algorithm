# 1806 부분합
import sys
input = sys.stdin.readline

# N= 수열 개수, S= 합 한계 , count = S 이상의 되는 부분합 개수
N, S = map(int, input().split())
arr= list(map(int, input().split()))
interval_sum = 0
length = int(1e9)
end = 0

for start in range(N):
  while interval_sum < S and end < N:
    interval_sum += arr[end]
    end+=1
  if interval_sum >= S:
     # 현재 interval_sum에 추가되지 않은 end가 있는 상태이므로 -1을 하고 계산
    length = min(length, (end-1)-start+1)
  interval_sum -= arr[start]

if length == 1e9:
  print('0')
else:
  print(length)
  
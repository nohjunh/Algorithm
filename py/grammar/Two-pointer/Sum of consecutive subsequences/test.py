#https://youtu.be/ttLRltNDiCo

"""
N = 데이터 수
M = 서치할 부분합
count = M을 만족하는 부분합의 수
"""
N = 5
M = 5
count = 0
data = [1, 2, 3, 2, 5]

interval_sum = 0
end = 0

for start in range(N):
  while interval_sum < M and end < N:
    interval_sum += data[end]
    end += 1
  if interval_sum == M:
    count += 1
  interval_sum -= data[start]

print(count)
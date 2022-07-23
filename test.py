N= int(input())
num_list= list(map(int, input().split()))

DP = [1 for _ in range(N)]

for i in range(N):
  for j in range(i):
    if num_list[j] < num_list[i]:
      DP[i] = max(DP[i], DP[j]+1)

print(max(DP))

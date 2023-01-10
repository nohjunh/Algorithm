#1182. 부분수열의 합
import sys
input = sys.stdin.readline

def dfs(idx, sum):
  global count
  if idx >= N:
    return
  sum+= arr[idx] # 이번 index번 쨰 수를 포함하는 경우
  if sum == S:
    count+=1
  dfs(idx+1, sum) # 이번 index번 째 수를 포함하고 다음으로 넘어가는 경우
  dfs(idx+1, sum-arr[idx]) # 이번 index번 째를 포함하지 않고 다음으로 넘어가는 경우
  

N, S = map(int, input().split())
arr= list(map(int, input().split()))
count= 0
sum = 0

dfs(0, 0)
print(count)
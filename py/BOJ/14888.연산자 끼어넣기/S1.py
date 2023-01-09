# 14888 연산자 끼어넣기
# https://data-flower.tistory.com/72
from sys import stdin
input = stdin.readline

def dfs(i, sum):
  global minSum, maxSum
  if i==N:
    minSum = min(minSum, sum)
    maxSum = max(maxSum, sum)
  else:
    # '+'
    if operNum[0] > 0:
      operNum[0]-=1
      dfs(i+1, sum+arr[i])
      operNum[0]+=1
    # '-'
    if operNum[1] > 0:
      operNum[1]-=1
      dfs(i+1, sum-arr[i])
      operNum[1]+=1
    # '*'
    if operNum[2] > 0:
      operNum[2]-=1
      dfs(i+1, sum*arr[i])
      operNum[2]+=1
    # '/'
    if operNum[3] > 0:
      operNum[3]-=1
      dfs(i+1, sum/arr[i])
      operNum[3]+=1

# N = 수의 갯수
N = int(input())
# 수열
arr = list(map(int, input().split()))
# 연산자 목록, [ +, -, *, / ]
operNum=list(map(int,input().split()))
minSum, maxSum= 1e9,-1e9

dfs(1, arr[0])
print(maxSum)
print(minSum)
import sys
input = sys.stdin.readline

def DFS(n, sum):
    global count
    if n == sum:
      count+=1
    elif n < sum:
       return
    DFS(n, sum+1)
    DFS(n, sum+2)
    DFS(n, sum+3)

T = int(input()) # 테스트케이스 갯수
for _ in range(T):
    n = int(input())
    count = 0
    DFS(n, 0)
    print(count)

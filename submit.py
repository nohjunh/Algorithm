#1992 쿼드트리
from sys import stdin
input = stdin.readline

def quadTree(x,y,n):
  global result
  if n==1:
    result+=graph[x][y]
    return;
  for row in range(x, x+n):
    for col in range(y, y+n):
      test = graph[x][y]
      if graph[row][col] != test:
        result += '('
        quadTree(x, y, n//2)
        quadTree(x, y+n//2, n//2)
        quadTree(x+n//2, y, n//2)
        quadTree(x+n//2, y+n//2, n//2)
        result += ')'
        return;
  result+=graph[x][y]

N= int(input())
result = ""
graph = [list(input().strip()) for _ in range(N)]
quadTree(0,0,N)
print(result)

#5639 이진 검색 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

def dfs(start, end):
  if start > end: # start index가 end index를 넘으면 그냥 리턴
    return
  
  rootValue = preOrder[start]

  # 루트 다음 노드부터 쭉 돌면서 루트보다 큰 값이 나오면
  # 거기가 오른쪽 서브트리의 루트
  nextIdx = start + 1 
  while nextIdx <= end:
    if rootValue > preOrder[nextIdx]:
      nextIdx+=1
    else:
      break
  
  dfs(start+1 ,nextIdx-1) # 왼쪽 서브트리
  dfs(nextIdx, end) # 오른쪽 서브트리
  print(rootValue)
  

preOrder= []
while True:
  try:
    preOrder.append(int(input()))
  except:
    break

dfs(0, len(preOrder)-1) # start와 end index

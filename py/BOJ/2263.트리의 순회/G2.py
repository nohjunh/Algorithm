# 2263 트리의 순회
# ref) https://ku-hug.tistory.com/135?category=978336
"""
postorder의 마지막이 현 트리의 root
inorder에서 루트를 찾고 루트 전까지가 왼쪽 subtree, 루트 후부터가 오른쪽 subtree
preorder 재귀를 하면서 매 단계마다 root 출력

ex) idx |  0 1 2 3       4 5  (노드 6개)
inorder :  4 2 5 1(root) 3 6
postorder: 4 5 2 6       3 1(root)
inorder의 왼쪽 subtree index 범위 = 0 ~ 2 (inStart, inStart+왼쪽subtree갯수-1)
inorder의 오른쪽 subtree index 범위 = 4 ~ 5 (inEnd-오른쪽subtree갯수+1, inEnd)
postorder의 왼쪽 subtree index 범위 = 0 ~ 2 (postStart, postStart+왼쪽subTree갯수-1)
postorder의 오른쪽 subtree index 범위 = 3 ~ 4 (postEnd-오른쪽subTree갯수,postEnd-1)
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # PyPy3
#sys.setrecursionlimit(10**6) # Python3

def preorder(inStart, inEnd, postStart,postEnd):
  if(inStart > inEnd) or (postStart > postEnd):
      return

  root= postOrder[postEnd]
  rootIdx= nodeIdx[root]  # root가 위치한 곳의 idx가 rootIdx
  # post의 왼,오 substree 갯수를 세기 위해 inOrder root를 기준으로 갯수 파악
  leftScope = rootIdx - inStart # 왼쪽 subtree 갯수
  rightScope= inEnd - rootIdx # 오른쪽 subtree 갯수

  print(root, end=' ')
  # (inOrder의 왼쪽 subtree index 범위, postOrder의 왼쪽 subtree index 범위)
  preorder(inStart, inStart+leftScope-1, postStart, postStart+leftScope-1)
  # (inOrder의 오른쪽 subtree index 범위, postOrder의 오른쪽 subtree index 범위)
  preorder(inEnd-rightScope+1, inEnd, postEnd-rightScope, postEnd-1)

# 정점번호
n= int(input())
inOrder= list(map(int, input().split()))
postOrder = list(map(int, input().split()))

nodeIdx= [0] * (n+1)
"""
 postOrder의 마지막이 현 트리의 root이므로
 inOrder 순서의 index를 저장하기 위함.
 nodeIdx[rootValue]= index 를 기준으로 index보다 작은 것들이 왼쪽 subtree, 큰 것들이 오른쪽 subtree
"""
for i in range(n):
  nodeIdx[inOrder[i]]=i

# tree index 0부터 시작
preorder(0, n-1, 0, n-1)
# 1991. 트리 순회
import sys
input = sys.stdin.readline

class Node():
  def __init__(self, Alpha, left, right):
    self.Alpha = Alpha
    self.left = left
    self.right = right
  
def preOrder(node):
  if node != None:
    print(tree[node].Alpha, end='')
    preOrder(tree[node].left)
    preOrder(tree[node].right)

def inOrder(node):
  if node != None:
    inOrder(tree[node].left)
    print(tree[node].Alpha, end='')
    inOrder(tree[node].right)

def postOrder(node):
  if node != None:
    postOrder(tree[node].left)
    postOrder(tree[node].right)
    print(tree[node].Alpha, end='')

# N = 이진 트리 노드의 갯수
N= int(input())
tree = {}

for _ in range(N):
  alpha, leftChild, rightChild = map(str, input().split())
  tree[alpha] =  Node(alpha, leftChild, rightChild)
  if leftChild == '.':
    tree[alpha].left = None
  if rightChild == '.':
    tree[alpha].right = None

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
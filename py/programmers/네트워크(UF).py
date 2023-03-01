def find_parent(parent, node):
  if parent[node] != node:
      parent[node] = find_parent(parent, parent[node])
  return parent[node]
  
def union_parent(parent, aNode, bNode):
  aNode_P = find_parent(parent, aNode)
  bNode_P = find_parent(parent, bNode)
  if aNode_P < bNode_P:
      parent[bNode_P] = aNode_P
  else:
      parent[aNode_P] = bNode_P

def solution(n, computers):
  parent = [0] * (n)
  for i in range(n):
      parent[i] = i
  for i in range(n):
      for j in range(n):
          if computers[i][j] == 1:
              union_parent(parent, i, j)
  answer = 0
  for i in range(n):
      if parent[i]==i:
          answer+=1
  return answer
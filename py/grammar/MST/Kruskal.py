# https://youtu.be/Gj7s-Nrt1xE

# 특정 원소가 속한 집합 찾기
def find_parent(parent, node):
  # 루트 노드를 찾을 때까지 재귀
  if parent[node] != node: # 같아야 루트
    parent[node] = find_parent(parent, parent[node])
  return parent[node]
   
# 두 원소가 속한 집합 union
def union_parent(parent, aNode, bNode):
  aNode_P = find_parent(parent, aNode)
  bNode_P = find_parent(parent, bNode)
  if aNode_P < bNode_P:
    parent[bNode_P] = aNode_P
  else:
    parent[aNode_P] = bNode_P
      
# V = 노드의 개수, E = 간선의 개수
V, E= map(int, input().split())
parent = [0] * (V+1) # 부모를 나타내는 테이블 (0번 제외)

edges = [] # 간선 리스트
resultCost = 0 # 비용

# 초기 부모테이블을 자기 자신이므로 초기화 과정 진행
for i in range(1, V+1):
  parent[i] = i

# 간선 정보 입력
for _ in range(E):
  aNode, bNode, cost = map(int, input().split())
  # 비용 순 정렬을 위해 cost를 튜플의 첫 번째로 지정
  edges.append( (cost, aNode, bNode) )

# 간선 정렬
edges.sort()

# cost가 낮은 간선부터 하나씩 사이클을 만드는지 여부를 확인하며 MST 구성 시작
for edge in edges:
  cost, aNode, bNode = edge
  # 사이클 여부 파악하고(부모가 같은데 union하면 사이클 형성)
  if find_parent(parent, aNode) != find_parent(parent, bNode):
    union_parent(parent, aNode, bNode)
    resultCost += cost

print(resultCost)

    
  
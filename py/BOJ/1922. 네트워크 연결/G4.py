# 1922 네트워크 연결
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, node):
  # 루트 노드를 찾을 때까지 재귀
  if parent[node] != node: # 같아야 루트
    parent[node] = find_parent(parent, parent[node])
  return parent[node]
   
# 두 원소가 속한 집합 union
def union_parent(parent, a_com, b_com):
  a_P = find_parent(parent, a_com)
  b_P = find_parent(parent, b_com)
  if a_P < b_P:
    parent[b_P] = a_P
  else:
    parent[a_P] = b_P

# N = 컴퓨터의 수
# M = 연결할 수 있는 선의 수
N = int(input())
M = int(input())
parent = [0] * (N+1) # 부모를 나타내는 테이블 (0번 제외)

edges = [] # 간선 리스트
resultCost = 0 # 비용

# 초기 부모테이블을 자기 자신이므로 초기화 과정 진행
for i in range(1, N+1):
  parent[i] = i

# 간선 정보 입력
for _ in range(M):
  a_com, b_com, cost = map(int, input().split())
  # 비용 순 정렬을 위해 cost를 튜플의 첫 번째로 지정
  edges.append((cost, a_com, b_com))

# 간선 정렬
edges.sort()

# cost가 낮은 간선부터 하나씩 사이클을 만드는지 여부를 확인하며 MST 구성 시작
for edge in edges:
  cost, a_com, b_com = edge
  # 사이클 여부 파악하고(부모가 같은데 union하면 사이클 형성)
  if find_parent(parent, a_com) != find_parent(parent, b_com):
    union_parent(parent, a_com, b_com)
    resultCost += cost

print(resultCost)
# union_find = 합집합 찾기 = 서로소 집합 알고리즘(Disjoint-Set)
# 다수의 노드들 중에 연결된 노드를 찾거나 노드들을 합칠때 사용하는 알고리즘
# 여러 개의 노드가 존재할 때 2개의 노드를 선택 -> 
# 이 2개의 노드가 같은 그래프에 속하는지 판별하는 알고리즘
# union(합침)과정: 2개의 노드를 연결할때 각 노드의 부모노드의 번호가 더 작은 쪽으로 합친다
# 재귀함수를 사용해 2개 이상의 노드가 연결되었을 때 하나의 부모노드의 번호를 가질 수 있도록 한다.
# Find(찾기)과정: 2개의 노드의 부모 노드를 확인 -> 현재 같은 집합에 속하는지 확인하는 알고리즘

# 구현부
# Union 연산 : 두 원소 a, b 가 주어질 때, 이들이 속한 두 집합을 하나로 합침
# Find 연산 : 어떤 원소 a 가 주어질 때, 이 원소가 속한 집합을 반환
# 1. find 함수로 해당 노드의 루트 노드를 찾는다.
# 2. union 함수로 두 노드의 루트 노드가 다르다면, 두 노드가 포함되어 있는 집합을 하나로 결합.
# 3. 만약, 루트 노드가 동일하다면 두 노드가 동일한 집합에 있는 것으로 판단하여 union 연산 수행 X
# https://8iggy.tistory.com/157

# union-find 배열 기반 구현
# Union연산: O(N) , Find연산 : O(1)
class disjointSet:

  def __init__(self, n):
    self.data= [i for i in range(n)]
    self.size= n # 집합의 갯수 (초기에는 각 노드가 하나의 집합이니 노드의 갯수로 지정)

  def find(self, idx):
    return self.data[idx]

  def union(self, x,y):
    x,y= self.find(x), self.find(y) # x, y 노드의 부모노드 탐색
    if x==y: # x,y노드의 부모노드가 같다면 즉, 같은 집합에 있다면
      return # union 연산을 수행하지 않음.
    for i in range(len(self.data)): #가리키는 부모노드가 같지 않다면, 다른 집합에 있다는 것이고
      # 두 집합을 합하기 위해 배열을 순회하면서 하나의 집합을 다른 하나의 집합 번호로 교체.
      if self.data[i]== y: # i번째 노드의 부모노드가 y노드의 부모노드와 같다면
        self.data[i]= x # i번쨰 노드의 부모노드에 x노드의 부모노드 값을 넣어서 같은 집합에 속하게 만든다.
    self.size-= 1

s = disjointSet(10)
s.union(0, 1)
s.union(2, 3)
s.union(1, 2)
s.union(0, 1)
s.union(4, 5)
s.union(5, 6)
s.union(7, 8)
s.union(7, 9)

print(s.data)
print(s.size)


# 트리로 Union-Find 구현
# 노드는 부모노드가 누구인지를 배열을 통해 담고,
# 각 Disjoint Set 트리의 루트 노드는 루트노드임을 알려주는 지표를 가짐
# Union 연산: 각 트리의 루트 노드를 찾은 뒤 다르면 한 쪽 트리의 루트 노드를 다른 한쪽의 루트 노드로 바꿔 자식에 넣음으로써 트리를 합합
# Find 연산: 각 노드의 저장된 부모 노드 정보를 따라 자기 자신이 부모로 갖는 루트 노드를 찾음
# Union : O(1)*O(h) / Find: O(h)

class disjointSet:
  def __init__(self, n):
    # 각자 다른 집합이 된다. 모두가 자기자신을 루트노드로 가짐.
    self.data= [-1 for _ in range(n)] # -1의 값을 가지면 루트노드라는 뜻
    self.size = n 
  def find(self, idx):
    parent = self.data[idx] # idx번 노드의 부모노드를 찾음
    if parent < 0: # 부모노드가 -1이라면 루트노드라는 것이므로
      return idx # 해당 idx번 노드가 루트노드임. 따라서 루트노드 index를 반환 
    return self.find(parent) # 루트노드가 아니니 재귀함수를 통해 해당 노드의 루트노드까지 찾음

  def union(self, x,y):
    x,y = self.find(x), self.find(y) # x,y노드의 부모노드를 찾음 (find함수니 루트노드까지 찾게 되는거.)
    if x==y: # 부모노드가 같다면
      return #union 함수 수행할 필요X
    self.data[y]=x # x노드의 부모노드를 y노드의 부모노드로 넣음 => 하나의 집합이 됨.
    self.size -= 1 # 집합이 하나로 합쳐졌으니 집합의 수 감소

s = disjointSet(10)
s.union(0, 1)
s.union(2, 3)
s.union(1, 2)
s.union(0, 1)
s.union(4, 5)
s.union(5, 6)
s.union(7, 8)
s.union(7, 9)

print(s.data)
print(s.size)
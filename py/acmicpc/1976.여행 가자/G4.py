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
    if x < y:
      self.data[y]=x # x노드의 부모노드를 y노드의 부모노드로 넣음 => 하나의 집합이 됨.
    else:
      self.data[x]=y
    self.size -= 1 # 집합이 하나로 합쳐졌으니 집합의 수 감소

  def check(self, ans):
    for i in range(len(ans)):
      ans[i]=self.find(ans[i]-1)
    comp= ans[0]
    for i in range(1, len(ans)):
      if ans[i]!=comp:
        return "NO"
    return "YES"

N= int(input())
M= int(input())
unionFind= disjointSet(N)
matrix=[]
for i in range(N):
  matrix.append(list(map(int, input().split())))

for i in range(N):
  for j in range(N):
    if matrix[i][j]==1:
      unionFind.union(i, j)

ans= list(map(int, input().split()))
print(unionFind.check(ans))
# WeightedQuickUnion

ids= []
size= []    # 각 객체를 root로 하는 tree의 크기 저장하는 배열

for idx in range(N):  ## ids 초기화
  ids.append(idx)
  size.append(1) 

def root(i):
  while i != ids[i]: ## root에 도달할 때까지 parent 따라 올라가기 
    i= ids[i]
  return i   ## i번쨰 컴포넌트 id가 i랑 같다면 root라는 뜻이고 root의 컴포넌트id 리턴

def connected(p, q):
  return root(p) == root(q) # p와 q가 같은 root를 가졌는지 확인

def union(p, q):
  id1, id2= root(p), root(q) # p,q노드의 루트값을 구하고
  if id1==id2:
    return # 루트 값이 같으면 이미 같은 집합이라는거니까 합칠 필요 x
  if size[id1] <= size[id2]: # p노드의 root노드를 root로 하는 tree의 크기가 q노드의 root tree보다 작으면
    ids[id1]= id2            # ids[id1] 즉, p노드의 root노드의 parent값으로 id2의 값을 넣어줌. => 두 컴포넌트가 합쳐짐
    size[id2] += size[id1]   # id1이 id2 아래로 들어간거니까 id2의 size에 id1의 size를 더해줌
  else:           # q가 속한 트리의 사이즈가 작은 경우           
    ids[id2] = id1
    size[id1] += size[id2]
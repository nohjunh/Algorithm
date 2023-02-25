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

def solution(n, wires):
    answer = 1e9
    
    for i in range(len(wires)):
        parent = [0] * (n+1)
        for k in range(1, n+1):
            parent[k] = k
            
        for j in range(len(wires)):
            if i == j:
                continue
            aNode, bNode = wires[j]
            union_parent(parent, aNode, bNode)
        
        for wire in wires:
            aNode, bNode = wire
            parent[aNode] = find_parent(parent, aNode)
            parent[bNode] = find_parent(parent, bNode)
            
        count_A = 1
        count_B = 0
        pivot = parent[1]
        for i in range(2, len(parent)):
            if pivot == parent[i]:
                count_A +=1
            else:
                count_B +=1
                
        answer = min(answer, abs(count_A-count_B))
    return answer

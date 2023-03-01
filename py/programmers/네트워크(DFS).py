def DFS(i, computers):
    global visited
    visited.append(i)
    for j, connected in enumerate(computers[i]):
        if j not in visited:
            if connected == 1:
                DFS(j, computers)
        
def solution(n, computers):
    global visited
    visited = []
    answer = 0
    for i in range(n):
        if i not in visited:
            DFS(i, computers)
            answer+=1
    return answer
def diff(prev, current):
    temp = 0
    for i in range(len(prev)):
        if prev[i] != current[i]:
            temp += 1
    if temp == 1:
        return True
    else:
        return False

def DFS(depth, count, begin, target):
    global wordsT, minCount
    if depth >= len(wordsT):
        return
    if begin == target:
        minCount = min(minCount, count)
        return
    for i in range(len(wordsT)):
        if diff(begin, wordsT[i]) and i not in visited:
            visited.append(i)
            DFS(depth+1, count+1, wordsT[i], target)
            visited.pop()
            
def solution(begin, target, words):
    global wordsT, visited, minCount
    wordsT= words[:]
    visited = []
    minCount = 1e9
    DFS(0, 0, begin, target)
    if minCount == 1e9:
        answer = 0
    else:
        answer = minCount
    return answer
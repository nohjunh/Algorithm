def DFS(depth, numbers, target):
    global answer
    if depth == len(numbers) and sum(numbers) == target:
        answer += 1
        return
    if depth >= len(numbers):
        return
    DFS(depth+1, numbers, target)
    numbers[depth] *= -1
    DFS(depth+1, numbers, target)

def solution(numbers, target):
    global answer
    answer = 0
    DFS(0, numbers, target)
    return answer
import sys
input = sys.stdin.readline

def DFS(depth, weight):
    global answer
    if depth == N:
        answer += 1
        return
    for i in range(N):
        if not visited[i] and weight >= 500:
            visited[i] = True
            DFS(depth + 1, weight + increment[i] - K)
            visited[i] = False

N, K = map(int, input().split())
increment = list(map(int, input().split()))
answer = 0
visited = [False] * (N)
DFS(0, 500)
print(answer)

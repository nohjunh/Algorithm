from collections import deque
def BFS(start, maps):
    global visited
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append(start)
    visited.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                visited.append((nx, ny))
    return maps

def solution(maps):
    global visited
    mapsTemp = maps[:]
    answer = 0
    visited = []
    mapsTemp = BFS((0, 0), mapsTemp)
    if (len(maps)-1, len(maps[0])-1) not in visited:
        answer = -1
    else:
        answer = mapsTemp[len(maps)-1][len(maps[0])-1]
    return answer
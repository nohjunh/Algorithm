# 16928
import sys
input=sys.stdin.readline
from collections import deque

# 보드판은 1~100까지의 수가 하나씩 적혀있는 10X10
board=[0]*101

# N=사다리의 수, M= 뱀의 수
N, M= map(int, input().split())

# 사다리와 뱀은 해당 좌표에 도착할 시 위치가 미리 저장된 곳으로 워프해야되므로
# 좌표 값을 쌍으로 저장하고 있어야 된다. -> 딕셔너리 이용
ladder= {}
snake= {}
for _ in range(N):
    a, b =map(int,input().split())
    ladder[a]=b
for _ in range(M):
    a, b= map(int, input().split())
    snake[a]=b

visited=[0 for _ in range(101)]

def BFS_adj_list(board):
    queue= deque([1])
    while queue:
        position = queue.popleft()
        if position==100: # 100번째 칸에 도착 -> 주사위를 몇 번 굴러야하는지 출력
            return board[100]
        # 주사위 값 1~6
        for value in range(1,7):
            move_value= position+value
            if 1<=move_value<=100 and visited[move_value]==0:
                # ladder딕셔너리의 key값들 중에 move_value가 있다면
                if move_value in ladder.keys():
                    move_value= ladder[move_value]
                # snake딕셔너리의 key값들 중에 move_value가 있다면
                if move_value in snake.keys():
                    move_value= snake[move_value]
                if visited[move_value]==0:
                    visited[move_value]= 1
                    board[move_value]= board[position]+1
                    queue.append(move_value)

print(BFS_adj_list(board))
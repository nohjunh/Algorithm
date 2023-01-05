# 14226
import sys
input=sys.stdin.readline
from collections import deque

# 스마일 이모티콘 S개
S= int(input())
# ex) 1>저장>붙여넣기 -> 2 >저장> 붙여넣기 -> 4 
# (ㅁ,ㅁ) => 현재 화면에 있는 이모티콘 갯수, 클립보드에 저장된 이모티콘
visited= {}
visited[(1,0)]=0 #이미 화면에 이모티콘 1개가 입력된 상황

def BFS_adj_list(visited):
    queue= deque([(1,0)]) 
    while queue:
        current_emoti, clipboard= queue.popleft()

        if current_emoti==S: # 현재 이모티콘 갯수가 S개 일때 
            return visited[(current_emoti, clipboard)]

        # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if (current_emoti, current_emoti) not in visited.keys(): 
            visited[(current_emoti,current_emoti)]= visited[(current_emoti,clipboard)]+1
            queue.append((current_emoti,current_emoti))
        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다
        if (current_emoti+clipboard, clipboard) not in visited.keys():
            visited[(current_emoti+clipboard, clipboard)]= visited[(current_emoti,clipboard)]+1
            queue.append((current_emoti+clipboard,clipboard))
        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        if (current_emoti-1, clipboard) not in visited.keys():
            visited[(current_emoti-1, clipboard)]= visited[(current_emoti,clipboard)]+1
            queue.append((current_emoti-1,clipboard))

print(BFS_adj_list(visited))
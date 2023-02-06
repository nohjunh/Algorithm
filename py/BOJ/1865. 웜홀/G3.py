# 1865. 웜홀
import sys
input = sys.stdin.readline
INF = 1e9

def bellman_ford(startNode):
  time[startNode] = 0
  for i in range(N):
    for j in range(len(edges)):
      typefor = edges[j][0] # road or hole
      start = edges[j][1] # S
      end = edges[j][2] # E
      cost = edges[j][3] # T
      # 음의 순환만 체크하면 되기에 time[start]의 INF 여부를 파악할 필요 X
      if typefor == "road":
        if time[end] > time[start] + cost:
          time[end] = time[start] + cost
          if i == N-1:
            return True
      else: # hole
        if time[end] > time[start] - cost:
          time[end] = time[start] - cost
          if i == N-1:
            return True
  return False
  
#테스트케이스 갯수
TC = int(input())
for _ in range(TC):
  # N= 지점의 수, M= 도로의 개수, W= 웜홀의 개수
  N, M, W = map(int, input().split())
  edges = []
  time = [INF] * (N+1)
  # 도로
  for _ in range(M):
    # S,E= 연결된 지점의 번호, T= 이동시간
    # 도로에는 방향이 없음
    S, E, T = map(int, input().split())
    edges.append(("road", S, E, T))
    edges.append(("road", E, S ,T))
  # 웜홀
  for _ in range(W):
    # S= 시작지점, E= 도착지점, T= 줄어드는 시간
    S, E, T = map(int, input().split())
    edges.append(("hole", S, E, T))
  
  negative_cycle = bellman_ford(1)
  if negative_cycle:
    print("YES")
  else:
    print("NO")
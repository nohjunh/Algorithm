# https://youtu.be/Ppimbaxm8d8
import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(startNode):
  # 시작노드부터 거리 초기화하고 시작
  dist[startNode] = 0
  """
  전체 n번 라운드 반복하는데 마지막 라운드에서는 값이 갱신되는지 파악해 음수 순환여부를 확정 짓는다.
  예를 들어, A->B로의 최단 경로의 크기는 주어진 노드의 갯수 -1 (n-1)개가 최대이다.
  만약 n-1를 넘는다면 중복된 노드를 또 방문한다는 것이고 이는 최단경로라 할 수 없으며, 음의 순환이 존재한다는 뜻이다.
  따라서, for문의 range는 0~N-2 (n-1개) 까지 최단경로 파악에 진행, N-1은 음의 순환 결정을 진행
  """
  for i in range(N):
    # 매 loop마다 모든 간선 확인
    for j in range(M):
      start = edges[j][0] # S
      end = edges[j][1] # E
      cost = edges[j][2] # T
      # 현재 간선을 거쳐 다른 노드로 가는 경우가 
      # 현 시점 다른 노드까지의 최단거리보다 더 최단일 경우
      if dist[start] != INF and dist[end] > dist[start] + cost:
        dist[end] = dist[start] + cost
        if i == N-1: # N-1번째 마저도 거리를 최단으로 갱신하는 경우가 존재한다면,
          return True # 음의 순환이 존재
  return False


# N= 노드의 개수, M = 간선의 개수
N, M = map(int, input().split())
# 벨만포드는 간선을 기준으로 하므로 간선정보를 담을 배열 생성
edges = []
# 최단거리 테이블 (0번 index 제외)
dist = [INF] * (N+1)

# 간선 정보
for _ in range(M):
    # start, end, time or distance
    S, E, T = map(int, input().split())
    # S -> E 의 비용 = T
    edges.append((S, E, T))

# 1번 노드부터 start. 간선 기준으로 loop 수행
# 음수 순환 여부가 벨만포드 알고리즘 리턴값
negative_cycle = bellman_ford(1)

if negative_cycle: # 음수 순환이 있다면
   print("-1")
else:
   # 시작노드인 1번 노드를 제외한 다른 모든 노드까지의 최단 거리 출력
   for i in range(2, N+1):
      if dist[i] == INF: # 도달불가능
         print("-1")
      else: # 도달 가능
         print(dist[i])
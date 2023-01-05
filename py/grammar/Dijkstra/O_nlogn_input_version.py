import heapq
import sys
input= sys.stdin.readline

INF= sys.maxsize # 무한을 의미하는 값

# 노드의 개수, 간선의 개수 입력받기
n,m =map(int, input().split())
# 시작 노드 번호 입력받기
start= int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph= [ [] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1) # 먼저, start로부터의 각 노드별 최단 거리를 INF로 초기화

# 모든 간선 정보 입력받기
for _ in range(m): # 간선의 개수 m개
  a, b, c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 거리는 0이고, 먼저 큐에 삽입
  heapq.heappush(q, (0, start)) # 두번째 요소의 첫번째=거리, 두번째= 목적지 노드
  distance[start] = 0 # start노드의 최단거리는 0
  while q: # 큐가 비어있지 않을 때까지 반복
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q) # 갱신되지 않은 가장 작은 거리 값을 가지는 거리정보와 노드정보를 꺼냄
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    # 처리된 적이 없다면 distance[now]는 INF값이므로 dist보다 무조건 큼
    # 따라서, continue가 아니라 for문을 통해 최단거리를 재설정해야함.
    # 또한, 만약 distance[now]가 갱신되었다고 해도 dist보다 작다면 
    # 정리) 현재 꺼낸 노드의 거리값이 테이블에 기록되어 있는 값보다 크다면 이미 처리된거
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    # ex) graph[now] 가 [(3, 4)] 라면,
    #     i[1]의 값은 4가 됨. 이 때의 4는 now노드에서 3번노드로 가는 거리비용
    for i in graph[now]:
      # i[1]은 거리값
      cost = dist + i[1] # 현재까지의 최단거리에다가 거쳐가는 거리를 더함
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]: # i[0]은 인접한 노드 즉 i[0]으로 가는 최단거리
        distance[i[0]] = cost
        # 값이 갱신될 때마다 힙에 넣어줌.
        heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 무한으로 출력
  if distance[i] == INF:
    print("INF")
  # 도달할 수 있으면
  else:
    print(distance[i])
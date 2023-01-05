import heapq
import sys
input= sys.stdin.readline

INF= sys.maxsize # 무한을 의미하는 값

# V=정점의 개수, E=간선의 개수 입력받기
V,E = map(int, input().split())

# 시작 정점의 번호가 주어짐
start= int(input())

# 각 정점에서 다른 정점로의 연결되어 있는 정보를 담는 리스트 만들기
graph= [ [] for _ in range(V+1)]

# 최단 경로 테이블을 모두 무한으로 초기화
distance = [INF] * (V+1) # 먼저, start로부터의 각 정점별 최단 거리를 INF로 초기화

# 모든 간선 정보 입력받기
for _ in range(E): # 간선의 개수 m개
  u, v, w = map(int, input().split())
  # u정점에서 v정점으로 가는 가중치 w인 간선이라는 의미
  graph[u].append( (v,w) )

def dijkstra(start):
  q = []
  # 출발정점으로 가기 위한 최단 비용은 0이고, 먼저 큐에 삽입
  heapq.heappush(q, (0, start)) # 두번째 요소의 첫번째=비용, 두번째= 도착정점
  distance[start] = 0 # 출발정점의 최단 비용은 0
  while q: # 큐가 비어있지 않을 때까지 반복
    # 가장 최단비용이 작은 정점에 대한 정보 꺼내기
    dist, now = heapq.heappop(q) # 갱신되지 않은 가장 작은 비용 정보와 정점정보를 꺼냄
    # 현재 정점이 이미 처리된 적이 있는 정점이라면 무시
    # 처리된 적이 없다면 distance[now]는 INF값이므로 dist보다 무조건 큼
    # 따라서, continue가 아니라 for문을 통해 최단거리를 재설정해야함.
    # 또한, 만약 distance[now]가 갱신되었다고 해도 dist보다 작다면 
    # 정리) 현재 꺼낸 정점의 비용값이 테이블에 기록되어 있는 값보다 크다면 이미 처리된거
    if distance[now] < dist:
      continue
    # 현재 정점와 연결된 다른 인접한 정점들을 확인
    # ex) graph[now] 가 [(3, 4)] 라면,
    #     i[1]의 값은 4가 됨. 이 때의 4는 now정점에서 3번 정점로 가는 비용
    for i in graph[now]:
      # i[1]은 거리값
      cost = dist + i[1] # 현재까지의 최단 거리에다가 거쳐가는 거리를 더함
      # 현재 정점을 거쳐서, 다른 정점으로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]: # i[0]은 인접한 정점 즉 i[0]으로 가는 최단 거리
        distance[i[0]] = cost
        # 값이 갱신될 때마다 힙에 넣어줌.
        heapq.heappush(q, (cost, i[0]))
      
# 다익스트라 알고리즘을 수행
dijkstra(start)

for i in range(1, len(distance)):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])

import heapq
import sys
input= sys.stdin.readline

INF= sys.maxsize # 무한을 의미하는 값

# N= 도시의 개수, M= 버스의 개수 입력받기
N= int(input())
M= int(input())

# 각 도시에서 다른 도시로의 연결되어 있는 정보를 담는 리스트 만들기
graph= [ [] for _ in range(N+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1) # 먼저, start로부터의 각 도시별 최단 비용을 INF로 초기화

# 모든 버스 정보 입력받기
for _ in range(M): # 버스의 개수 m개
  a, b, c = map(int, input().split())
  # a번 도시(출발도시)에서 b번 도시(도착도시)로 가는 비용이 c라는 의미
  graph[a].append((b,c))

# 출발도시 및 도착도시 번호 입력받기
start, destination= map(int, input().split())

def dijkstra(start):
  q = []
  # 출발 도시로 가기 위한 최단 비용은 0이고, 먼저 큐에 삽입
  heapq.heappush(q, (0, start)) # 두번째 요소의 첫번째=비용, 두번째= 도착도시
  distance[start] = 0 # 출발도시의 최단 비용은 0
  while q: # 큐가 비어있지 않을 때까지 반복
    # 가장 최단비용이 작은 도시에 대한 정보 꺼내기
    dist, now = heapq.heappop(q) # 갱신되지 않은 가장 작은 비용 정보와 도시정보를 꺼냄
    # 현재 노드가 이미 처리된 적이 있는 도시라면 무시
    # 처리된 적이 없다면 distance[now]는 INF값이므로 dist보다 무조건 큼
    # 따라서, continue가 아니라 for문을 통해 최단비용을 재설정해야함.
    # 또한, 만약 distance[now]가 갱신되었다고 해도 dist보다 작다면 
    # 정리) 현재 꺼낸 도시의 비용값이 테이블에 기록되어 있는 값보다 크다면 이미 처리된거
    if distance[now] < dist:
      continue
    # 현재 도시와 연결된 다른 인접한 도시들을 확인
    # ex) graph[now] 가 [(3, 4)] 라면,
    #     i[1]의 값은 4가 됨. 이 때의 4는 now도시에서 3번 도시로 가는 비용
    for i in graph[now]:
      # i[1]은 비용값
      cost = dist + i[1] # 현재까지의 최단 비용에다가 거쳐가는 비용을 더함
      # 현재 도시를 거쳐서, 다른 도시로 이동하는 비용이 더 짧은 경우
      if cost < distance[i[0]]: # i[0]은 인접한 도시 즉 i[0]으로 가는 최단 비용
        distance[i[0]] = cost
        # 값이 갱신될 때마다 힙에 넣어줌.
        heapq.heappush(q, (cost, i[0]))
      
# 다익스트라 알고리즘을 수행
dijkstra(start)

print(distance[destination])
# 다익스트라_test
# heap 활용
# O(nlogn)

import sys
import heapq

# graph로 거리정보를 넣고 start에 해당 거리정보를 가진 노드이름
def dijkstra(graph, start):
  distances= {node_name: sys.maxsize for node_name in graph}
   # 딕셔너리니까 []와 =를 이용하면 key에 해당하는 value를 저장할 수 있음
   # 시작 노드의 거리는 0으로 설정
  distances[start]= 0
  queue = []
  # 힙 구조에 시작노드부터 탐색 시작하기 위해 시작노드의 거리부터 먼저 넣음
  # [거리, 노드이름] 순으로 넣는 이유: heapq모듈은 첫 번째 데이터를 기준으로 정렬을 진행함.
  heapq.heappush(queue, [distances[start], start])

  while queue: # queue에 남아있는 노드가 없을 때까지 반복
    # 탐색할 노드의 거리, 탐색할 노드의 이름을 가져옴
    # 즉, 가장 낮은 거리를 가진 노드의 거리와 노드이름을 가져옴
    current_node_distance, current_node_name = heapq.heappop(queue)
    
    # 기존에 있는 거리보다 길다면, 그냥 넘어감 (최단거리를 구하는 것이기 때문)
    if distances[current_node_name] < current_node_distance:
      continue

    for new_destination, new_distance in graph[current_node_name].items():
      # 해당 노드를 거칠 때의 거리
      distance = current_node_distance + new_distance
      if distance < distances[new_destination]:
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])
    
  return distances

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(sys.maxsize)
print(dijkstra(graph, 'A'))
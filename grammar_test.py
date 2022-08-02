
graph= [ [] for _ in range(5+1)]
a,b,c= map(int, input().split())

graph[a].append( (b,c) )

print(graph[a])
for i in graph[a]:
    print(i[0])

import sys
INF=sys.maxsize
distance = [INF] * (5+1) # 먼저, start로부터의 각 노드별 최단 거리를 INF로 초기화
print(distance)
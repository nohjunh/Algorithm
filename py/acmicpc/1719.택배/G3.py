import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 집하장의 개수, M= 집하장간 경로의 개수
N,M= map(int,input().split())

# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(N+1) for _ in range(N+1)] # 0번 인덱스는 사용하지 않음
ans_matrix=[[INF]*(N+1) for _ in range(N+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# 자기 자신에서 자기 자신으로 가는건 -로 처리
for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            graph_matrix[i][j]=0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            ans_matrix[i][j]='-'

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int, input().split())
    graph_matrix[a][b]=c
    graph_matrix[b][a]=c
    # a->b로 갈 떄 제일 먼저 b를 거쳐가야함
    # b->a로 갈 때 제일 먼저 a를 거쳐가야함
    ans_matrix[a][b]=b
    ans_matrix[b][a]=a
# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, N+1): # 거쳐가는 정점
    for i in range(1, N+1): # 시작 정점
        for j in range(1, N+1): # 도착 정점
          if graph_matrix[i][j] > graph_matrix[i][k]+graph_matrix[k][j]:
            graph_matrix[i][j]=graph_matrix[i][k]+graph_matrix[k][j]
            # i->j로 갈때 k를 거쳐서 가는게 더 빠르다면
            # i->k로 갈때 제일 먼저 거치는 값을 ans_matrix에 넣어줘야
            # i->j로 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야하는 집하장이 된다.
            # 즉, i->j로 가기위한 최단 경로는 i->k->j 이고 제일 먼저 거쳐가는 집하장을 구해야 하므로
            # i->k의 경로에서 제일 먼저 거쳐가는 집하장 값을 나타내는
            # ans_matrix[i][k]를 갱신하면 되는 것이다.
            ans_matrix[i][j]= ans_matrix[i][k]
            
# 수행 결과 출력
for i in range(1, N+1):
    for j in range(1, N+1):
      print(ans_matrix[i][j], end=' ')
    print()


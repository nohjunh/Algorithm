# 11404
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 도시의 갯수,  M= 버스의 갯수
N= int(input())
M= int(input())
# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(N+1) for _ in range(N+1)] # 0번 인덱스는 사용하지 않음

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            graph_matrix[i][j]=0

# 버스에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    # A(시작 도시)에서 B(도착 도시)로 가는 비용은 C라고 설정
    a,b,c = map(int, input().split())
    # 시작도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있기에 그 비교를 해줌.
    if graph_matrix[a][b] > c :
        graph_matrix[a][b]=c

# 점화식에 따라 플로이드 알고리즘 수행
for k in range(1, N+1): # 거쳐가는 정점
    for i in range(1, N+1): # 시작 정점
        for j in range(1, N+1): # 도착 정점
            # i에서 j로 바로 가는 것보다 i에서 k + k에서 j로 가는 값 중 더 작은 값을 i에서 j로 가는 경로의 값으로 설정
            graph_matrix[i][j]= min(graph_matrix[i][j], graph_matrix[i][k]+graph_matrix[k][j])

# 수행 결과 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        # 도달할 수 없는 것들은 0으로 출력
        if graph_matrix[i][j]==INF:
            print("0", end=' ')
        else:
            print(graph_matrix[i][j], end=' ')
    print()

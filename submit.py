# 1956 운동
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# V= 마을의 개수 , E= 도로의 갯수
# 도로는 일방 통행 -> 단방향
V,E= map(int, input().split())

# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(V+1) for _ in range(V+1)] # 0번 인덱스는 사용하지 않음

# 각 도로에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(E):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int, input().split())
    graph_matrix[a][b]=c

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, V+1): # 거쳐가는 마을
    for i in range(1, V+1): # 시작 마을
        for j in range(1, V+1): # 도착 마을
            # i에서 j로 바로 가는 것보다 i에서 k + k에서 j로 가는 값 중 더 작은 값을 i에서 j로 가는 경로의 값으로 설정
            graph_matrix[i][j]= min(graph_matrix[i][j], graph_matrix[i][k]+graph_matrix[k][j])

ans=INF
# 수행 결과 출력
# graph_matrix[i][i] => 사이클이므로 i에서 i까지의 비용값을 비교하면 됨.
for i in range(V):
    if ans > graph_matrix[i][i]:
        ans=graph_matrix[i][i]

if ans==INF:
    # 운동 경로를 찾지 못하는 경우
    print("-1")
else:
    print(ans)
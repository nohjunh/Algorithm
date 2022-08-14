# 1613 역사
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 사건의 개수, 알고 있는 사건의 전후 관계의 개수 k
N,M = map(int, input().split())
# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(N+1) for _ in range(N+1)] # 0번 인덱스는 사용하지 않음
# 앞에 일어난 사건인지 뒤에 일어난 사건인지 파악하기 위한 배열
first_matrix=[[INF]*(N+1) for _ in range(N+1)]

# 각 사건 전후 관계에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    # A,B 순으로 받으면
    # A가 B보다 먼저 일어났다는 것.
    a,b = map(int, input().split())
    graph_matrix[a][b]= 1
    # graph_matrix에 값이 있다는 건 두 사건의 전후관계를 파악할 수 있다는 거고
    # first_matrix를 통해 A사건이 먼저 일어났는지, B사건이 먼저 일어났는지를 체크한다.
    first_matrix[a][b]= -1
    first_matrix[b][a]= 1

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, N+1): # 거쳐가는 정점
    for i in range(1, N+1): # 시작 정점
        for j in range(1, N+1): # 도착 정점
            graph_matrix[i][j]= min(graph_matrix[i][j], graph_matrix[i][k]+graph_matrix[k][j])
            # graph_matrix[i][j]가 INF가 아니라는거는 두 사건의 전 후 관계를 파악할 수 있다는 거고
            # first_matrix로 전 후 사건을 파악한다.
            # i가 j사건보다 먼저 일어났으므로 -1
            # j가 i보다 늦게 일어났으므로 1
            if graph_matrix[i][j]!=INF:
                first_matrix[i][j]=-1
                first_matrix[j][i]=1

# s줄에는 각각 서로 다른 두 사건의 번호가 주어지고
# S줄에 걸쳐 
# 두 사건 중 앞에 있는 사건이 먼저 일어났으면 -1
# 뒤에 있는 사건이 먼저 일어났으면 1
# 전후 사건을 파악할 수 없으면 0 을 출력
S= int(input())
for i in range(S):
    a,b = map(int, input().split())
    if first_matrix[a][b]==INF:
        print("0")
    if first_matrix[a][b]==1:
        print("1")
    if first_matrix[a][b]==-1:
        print("-1")
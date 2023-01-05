# 1389
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 유저의 수,  M= 친구 관계의 수
N,M= map(int, input().split())

# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(N+1) for _ in range(N+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph_matrix[i][j]=0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    # A와 B가 친구일때 1라고 설정
    # B와 A도 친구
    a,b= map(int, input().split())
    graph_matrix[a][b]=1
    graph_matrix[b][a]=1

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1,N+1): # 거쳐가는 사람
    for i in range(1,N+1): # 시작 사람
        for j in range(1,N+1): # 도착 사람
            if i==j:
                continue
            else:
                graph_matrix[i][j]=min(graph_matrix[i][j], graph_matrix[i][k]+graph_matrix[k][j])

# 수행 결과 출력
ans=10000000
ans_person=0
for i in range(1, N+1):
    total=0
    for j in range(1, N+1):
      total+=graph_matrix[i][j]
    if ans>total:
        ans=total
        ans_person=i

print(ans_person)

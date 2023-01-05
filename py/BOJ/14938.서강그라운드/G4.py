# 14938 서강그라운드
from lib2to3.refactor import get_fixers_from_package
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 지역의 개수,  M= 수색범위, R= 길의 갯수
N,M,R= map(int, input().split())
# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(N) for _ in range(N)] # 0번 인덱스는 사용하지 않음

# 각 지역에 있는 아이템의 수
item_value=[0 for _ in range(N)]
value= list(map(int,input().split()))
for i in range(N):
    item_value[i]=value[i]

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(R):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,l = map(int, input().split())
    # 양방향 통행이 가능
    graph_matrix[a-1][b-1]=l
    graph_matrix[b-1][a-1]=l

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(N):
    for j in range(N):
        if i==j:
            graph_matrix[i][j]=0

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(N): # 거쳐가는 정점
    for i in range(N): # 시작 정점
        for j in range(N): # 도착 정점
                graph_matrix[i][j]= min(graph_matrix[i][j], graph_matrix[i][k]+graph_matrix[k][j])

ans_list=[]
for i in range(N):
    ans=0
    for j in range(N):
        if graph_matrix[i][j]<=M:
            ans+=item_value[j]
    ans_list.append(ans)

# 예은이가 얻을 수 있는 최대 아이템 개수를 출력
print(max(ans_list))

# 1507 궁금한 민호
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 도시의 갯수,  M= 도로의 갯수
N= int(input())
# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[]
# 정상 도로정보면 1
road_matrix=[[1]*(N) for _ in range(N)]

# 각 도로에 대한 정보를 입력 받아, 그 값으로 초기화
# 이 값은 도시 쌍에 대한 "최소" 이동 시간.
for _ in range(N):
    graph_matrix.append(list(map(int, input().split())))

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(N): # 거쳐가는 정점
    for i in range(N): # 시작 정점
        for j in range(N): # 도착 정점
            #자기 자신에서 자기로 가는 경우는 제외
            if i==j or i==k or j==k:
                continue
            # i->j가 i->k->j 의 값과 같다면 최소 도로의 갯수가 아님
            # i->j로 가는 도로는 필요없는 도로라고 칭함.
            # -> 사실 i->j로 바로 가는 도로는 없는 것이지만, 알고리즘 상에서는 있는 것처럼 보이기 때문
            # -> i->k->j로 인해 i->j의 도로가 생기는 것과 같은 원리 -> 이러한 도로를 없애주는 것이다.
            if graph_matrix[i][j]==graph_matrix[i][k]+graph_matrix[k][j]:
                road_matrix[i][j]=0
            # [i][j]가 더 크면 잘못된 정보
            if graph_matrix[i][j] > graph_matrix[i][k]+graph_matrix[k][j]:
                #불가능한 경우에는 -1을 출력한다.
                print("-1")
                exit()

ans=0
for i in range(N):
    for j in range(i,N):
        if road_matrix[i][j]!=0:
            ans+=graph_matrix[i][j]

print(ans)
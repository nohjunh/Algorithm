# 10159 저울
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 물건의 갯수,  M= 미리 측정된 물건 쌍의 개수
N= int(input())
M= int(input())

# 2차원 배열->그래프 만들고 모든 값을 INF으로 초기화
graph_matrix=[[INF]*(N) for _ in range(N)] # 0번 인덱스는 사용하지 않음

# 자기 자신은 비교 못하므로 INF로 그대로 나둠
for i in range(N):
    for j in range(N):
        if i==j:
            graph_matrix[i][j]=INF

# 각 물건에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    # a,b => a->b 즉, a는 b보다 무겁다.
    a,b= map(int, input().split())
    graph_matrix[a-1][b-1]= 1 # 1로 셋팅된 값은 무게 비교가 가능하다는 것  

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(N): # 거쳐가는 물건
    for i in range(N): # 시작 물건
        for j in range(N): # 도착 물건
            if graph_matrix[i][k]!=INF and graph_matrix[k][j]!=INF:
                graph_matrix[i][j]= 1

ans_matrix=[[INF]*(N) for _ in range(N)]


for i in range(N):
    for j in range(N):
        if i==j:
            # 구현의 정확성을 위해 자기 자신은 비교 가능하다고 check
            ans_matrix[i][j]=1
        if graph_matrix[i][j]== 1:
            ans_matrix[i][j]=1
            ans_matrix[j][i]=1

for i in range(N):
    count=0
    for j in range(N):
        if i==j:
            #자기 자신은 제외
            continue
        # 물건 i와 비교 결과를 알 수 없는 물건의 개수를 출력하기 위한 조건문 
        if ans_matrix[i][j]==INF:
            count+=1
    print(count)
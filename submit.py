# 2660 회장뽑기
from lib2to3.refactor import get_fixers_from_package
import sys
input= sys.stdin.readline
INF= int(1e9) # 무한

# N= 회원의 수 
N= int(input())
# 2차원 배열->그래프 만들고 모든 값을 무한으로 초기화
graph_matrix=[[INF]*(N) for _ in range(N)] # 0번 인덱스는 사용하지 않음

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
while(True):
    # 회원번호 A,B는 서로 친구 관계
    a,b= map(int, input().split())
    if a==-1 and b==-1:
        break
    # a와 b가 친구 사이면 1을 줌.
    graph_matrix[a-1][b-1]=1
    # b와 a도 친구 사이
    graph_matrix[b-1][a-1]=1

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

level=[]
# 각 회원 별 점수 중 최댓값 찾기
for i in range(N):
    level.append(max(graph_matrix[i]))
min_value=min(level)
# 회장 후보의 점수와 후보의 수를 출력
print(min_value, level.count(min_value))
# 회장 후보를 오름차순으로 모두 출력
# index를 0부터 시작했으므로 i+1로 출력한다. 그래야 1번회원부터의 탐색결과가 나옴
for i in range(N):
    if level[i]==min_value:
        print(i+1, end=' ')
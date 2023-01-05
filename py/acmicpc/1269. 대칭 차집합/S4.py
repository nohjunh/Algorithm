A, B= map(int, input().split())
A_set= set(map(int, input().split()))
B_set= set(map(int, input().split()))
A_B= A_set^B_set # set집합 대칭차집합 연산

print(len(A_B))
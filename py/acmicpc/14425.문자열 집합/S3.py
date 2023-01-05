#14425
import sys
input= sys.stdin.readline

N,M= map(int, input().split())
s_set= set(input() for _ in range(N))
count= 0
for i in range(M):
    test=input()
    if test in s_set:
        count+=1
print(count)
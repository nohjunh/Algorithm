N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A를 set으로 하면 순서를 신경 안쓰므로 시간복잡도 성능 개선
for i in B:
    if i in A:
        print("1")
    else:
        print("0")
 


    



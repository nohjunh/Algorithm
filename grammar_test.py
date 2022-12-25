# 코딩테스트 Good Code #Part 2

# 1-1. 최대, 최소 우아하게 범위 지정
# from sys import stdin, stdout, maxsize
# ans = maxsize
# minsize = -maxsize
# print(ans)
# print(minsize)

# 1-2. 진법 연산
# 3
# 1001101 10010
# 1001001 11001
# 1000111 1010110
# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write
# for _ in range(int(input())):
  # A, B = map(int, input().split())
  # print(bin(A)+bin(B))

# 3-1. 문자열 거꾸로
# str = "ABCD"
# print(str)
# reverseStr = str[::-1]
# print(reverseStr)

# 4-1. 배열 초기화
# 3 5
# 가로 3, 세로 5인 graph 배열로 생성
# from sys import stdin
# input = stdin.readline
# N, M = map(int, input().split())
# arr = [[0]*N for _ in range(M)]
# print(arr)

# 4-2 배열의 원소를 거꾸로
# arr = [1,2,3,4]
# print(arr)
# arr.reverse()
# print(arr)

# 4-3. 배열 특정 원소 갯수
# arr = [1,2,3,3,4]
# print(arr.count(3))

# 4-4. 원소 중복 제거
# set을 이용해서 처리한다. set은 중복값을 허용하지 않음, 원소의 순서도 고려하지 않음.
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ] 
# print(alpha)
# alpha = list(set(alpha))
# print(alpha)

# 2차원 리스트에서 중복된 리스트를 제거하려면
# lst = [[1,2], [1,2], [1]] 
# print(list(set(map(tuple, lst))))

# 4-5. 배열 정렬
# arr= [32,2,4,6]
# print(arr)
# arr.sort() # 오름차순
# print(arr)
# arr.sort(reverse=True) # 내림차순
# print(arr)

# 4-5-1. 좌표 정렬하기
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
# arr = []
# for _ in range(int(input())):
#  arr.append( list(map(int, input().split())) )
# x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순으로 정렬
# arr.sort(key=lambda x:(x[0], x[1]))
# for str in arr:
#  print(str[0], str[1])
# x좌표가 감소하는 순으로, x좌표가 같으면 y좌표가 감소하는 순으로 정렬
# arr.sort(key=lambda x:(-x[0], -x[1]))
# for str in arr:
#  print(str[0], str[1])


# 5-1. 파이썬 삼항
# a, b = map(int, input().split())
# print(a,b)
# a,b 중 더 큰 값을 res에 저장
# res = a if a > b else b
# print(res)

# arr= [1,2,3]
# res = len(arr) if arr.count(3)==5 else print("False")
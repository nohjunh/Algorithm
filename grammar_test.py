# 코딩테스트 Good Code #Part 1

# 1-1. 나누어 입력 받기
#a, b = map(int, input().split())

# 1-2. 입력 출력 가속
#from sys import stdin, stdout
#input = stdin.readline
#print = stdout.write

# 2-1. 우아한 배열 입력
# 3
# 1 2 3
# 4 5 6
# 7 8 9
#graph = [list(map(int, input().split())) for _ in range(int(input()))]

# 2-2. 정수와 배열이 같은 줄에 들어오는 경우
# 4 10 20 30 40
# 3 7 5 12
# 3 122 21 43
# 변수 앞에 *을 붙이면 뒤이어 나오는 값이 배열 형태로써 변수에 저장.
# N, *arr = map(int, input().split())

# 2-3. 문자열을 한 글자씩 배열에 저장
# 3
# AAAA
# BBBB
# CCCC
# list를 input 앞에 붙이면 input문자열을 글자 단위로 나눠서 저장.
# arr = [list(input()) for _ in range(int(input()))]

# 3-1. 배열을 연결해서 출력 1
# arr = [1,2,3,4] -> 1234로 출력
# map함수로 arr에 저장되어 있는 정수 값을 string타입으로 타입변환한 후 "".join으로 공백없이 값 출력
# arr= [1,2,3,4]
# print("".join(map(str,arr)))

# 3-2. 배열을 연결해서 출력 2
# 배열에서 요소를 각각 출력하는 방법 -> 띄어쓰기까지 가능
# arr = [1,2,3,4]
# print(*arr)


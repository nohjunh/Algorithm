# 2166 다각형의 면적
# ref) https://ko.wikihow.com/다각형 넓이 구하기/변의 길이가 다른 다각형 넓이 구하기
import sys
input = sys.stdin.readline
N= int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.append(points[0])

sum1= 0
sum2= 0
for i in range(1, len(points)):
  sum1 += points[i-1][0] * points[i][1]
  sum2 += points[i-1][1] * points[i][0]
print(abs(round((sum1-sum2)/2, 1)))
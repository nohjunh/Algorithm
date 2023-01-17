# 2110 공유기 설치
# ref) https://hongcoding.tistory.com/3
import sys
input = sys.stdin.readline

# N= 집의 개수, C= 공유기 개수
N, C = map(int, input().split())
maxValue = 0 # 가장 인접한 두 공유기 사이의 거리
house = []
for _ in range(N):
  house.append(int(input()))
house.sort()
"""
1~50번까지에서 원하는 수를 찾기 위해 이진탐색을 이용하는 것과 같은 원리
이분탐색을 공유기 사이의 거리를 정하는 것에 사용하는 문제
가장 왼쪽 집에 공유기를 하나 박고 시작해야 각 공유기들의 거리를 최대로 설치할 수 있음.
"""
start = 1 # 두 공유기 사이의 최소 간격
end = house[-1] - house[0] # 두 공유기 사이의 최대 간격
"""
# 두 공유기 사이의 간격을 가정해 (start+end)//2 = mid로 잡고
# mid보다 크다는 것은 mid 이상의 간격을 두고 설치가 가능하다는 소리
# mid보다 작은 곳에는 공유기 설치 불가
# 만약 mid로 두 공유기 사이의 거리를 정했을 때 C개보다 더 설치할 수 있다면,
# 두 공유기 사이의 간격을 넓혀서 다시 수행하면 되고 (그래야 최대거리를 구할 수 있으므로)
# C개보다 더 적게 설치된다면 두 공유기 사이의 간격을 좁혀서 수행해야 한다.
"""
while start <= end:
  count = 1 # 공유기 개수 (맨처음 박고 시작)
  lastHouseValue= house[0]
  mid = (start+end)//2
  for i in range(N):
    if house[i] - lastHouseValue >= mid:
      count+=1
      lastHouseValue= house[i]
  if count >= C:
    maxValue = mid
    start = mid+1
  else:
    end = mid -1
print(maxValue)
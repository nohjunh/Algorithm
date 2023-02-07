"""
N = 데이터 수
M = 서치할 부분합
count = M을 만족하는 부분합의 수
"""
N = 5
M = 5
count = 0
data = [1, 3, 2, 5, 4]
end = 0

data.sort() # 오름차순 만들어주고 시작

left, right = 0, N-1
while left < right:
  twoPointSum = data[left] + data[right]
  if twoPointSum == M:
    count+=1
    left += 1
  elif twoPointSum < M:
    left += 1
  else:
    right -= 1
    
print(count)
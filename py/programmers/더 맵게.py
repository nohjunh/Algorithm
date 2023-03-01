import heapq
def checkScoville(scoville, K):
    for i in range(len(scoville)):
        if scoville[i] < K:
            return True
    return False

def solution(scoville, K):
    data = []
    count = 0
    for i in range(len(scoville)):
        heapq.heappush(data, scoville[i])
    while checkScoville(data, K):
        if len(data) < 2: # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            count = -1
            break
        first = heapq.heappop(data)
        second = heapq.heappop(data)
        heapq.heappush(data, first+second*2)
        count += 1
    answer = count
    return answer
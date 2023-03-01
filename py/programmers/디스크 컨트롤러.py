import heapq

def solution(jobs):
    temp = []
    answer = 0
    start, end, count = -1, 0, 0
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                comeT, useT = job
                heapq.heappush(temp, [useT, comeT])
        if len(temp) > 0:
            useT, comeT = heapq.heappop(temp)
            start = end
            end = end + useT
            answer += (end - comeT)
            count += 1
        else:
            end+=1
            
    return answer//len(jobs)
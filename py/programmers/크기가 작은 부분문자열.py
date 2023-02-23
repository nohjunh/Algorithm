def solution(t, p):
    intervalCount = 0
    end = 0
    ans = []
    str = ""
    for start in range(len(t)):
        while intervalCount < len(p) and end < len(t):
            intervalCount += 1
            str += t[end]
            end += 1
        if intervalCount == len(p):
            ans.append(str)
        str = str[1:]
        intervalCount -= 1
    
    answer = 0
    for i in ans:
        if i <= p:
            answer+=1
    return answer
        

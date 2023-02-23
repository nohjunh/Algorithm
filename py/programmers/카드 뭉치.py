def solution(cards1, cards2, goal):
    answer = []
    idx1, idx2 = 0, 0
    for str in goal:
        if idx1 < len(cards1) and str == cards1[idx1]:
            idx1 += 1
            answer.append(str)
        elif idx2 < len(cards2) and str == cards2[idx2]:
            idx2 += 1
            answer.append(str)
        if goal == answer:
            return "Yes"
    return "No"

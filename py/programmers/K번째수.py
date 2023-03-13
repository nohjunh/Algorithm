def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[:]
        i, j, k = command
        arr = arr[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer
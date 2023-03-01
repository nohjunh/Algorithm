# ref) https://esoongan.tistory.com/103
def solution(numbers):
    temp = [str(numbers[i]) for i in range(len(numbers))]
    temp.sort(key = lambda x: x*3, reverse = True)
    answer = int(''.join(temp))
    return str(answer)
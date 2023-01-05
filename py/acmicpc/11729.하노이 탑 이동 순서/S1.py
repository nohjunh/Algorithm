num = int(input())

def hanoi(n, _from, to, mid):
	if n == 1: ## 3번기둥으로
		print(_from, to) ## to 가 3번기둥
		return

	hanoi(n-1, _from, mid, to) ## 1번 기둥의 n-1개의 원판을 2번 기둥으로
	print(_from, to) ## 1번 기둥에서 남은 원판을 3번 기둥으로
	hanoi(n-1, mid, to, _from) ## 2번 기둥의 n-1개의 원판 3번 기둥으로

print(2**num-1)  ## 이동 횟수 = 2^num -1
hanoi(num, 1, 3, 2)
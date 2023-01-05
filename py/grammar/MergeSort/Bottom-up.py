# Top-down merge-sort는 함수 호출/ 반환 과정에서 함수 인자, 지역변수 등을
# 메모리에 저장/ 삭제를 하는 과정을 반복하게 된다.
# 따라서, 이러한 과정을 통한 시간/공간 Overhead가 크게 된다.
# Bottom-up Merge Sort를 통해 Divide를 위한 재귀 호출 과정을 생략하여 Merge로만 sorting이 되도록 진행한다.
# sz=1에서 시작
# 크기 sz인 인접한 부분집합끼리 병합 -> sz 2배하고 sz>=N이 될 때까지 반복

# Copyright by Sihuing Lee


def merge(a, aux, lo, mid, hi):
    for k in range(lo, hi+1):
        aux[k] = a[k] # 예비 배열에 a[k]를 옮김 -> a[k]를 결과배열로 쓰기 위함.
        # 단, 어차피 배열을 인자로 전달하는 것이므로 주소를 복사할 것임. 즉, 새로 배열을 만드는 과정이 아니라
        # 정렬 결과를 바로바로 a[]에 적용시키는 것임.
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i>mid: a[k], j = aux[j], j+1            
        elif j>hi: a[k], i = aux[i], i+1            
        elif aux[i] <= aux[j]: a[k], i = aux[i], i+1
        else: a[k], j = aux[j], j+1            

    return a

def mergeSort(a):
    aux = [None] * len(a)

    sz = 1
    while( sz < len(a) ):
        for lo in range(0, len(a)-sz, sz*2):
            merge(a, aux, lo, lo+sz-1, min(lo+sz+sz-1, len(a)-1))            
        sz += sz  # 2배 -> 2배 -> 2배 ...

    return a

if __name__ == "__main__":
    print(mergeSort([10, 9, 3, 2, 6, 7]))

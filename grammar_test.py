# 15663
# permutations함수 이용

import itertools
import sys
from itertools import permutations
input= sys.stdin.readline


N, M= map(int, input().split())
num_list=list(map(int, input().rstrip().split()))
ans=itertools.permutations(num_list, M)
ans_list=sorted(list((set(ans))))
for i in ans_list:
  print(*i)
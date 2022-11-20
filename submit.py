# 5430 AC
import re
import sys
from collections import deque

T= int(sys.stdin.readline())
for _ in range(T):
  reverse= False
  check= False

  inputFunction = sys.stdin.readline()
  n = int(sys.stdin.readline())
  inputNumber= sys.stdin.readline().rstrip()[1:-1].split(',')
  if n==0:
    inputNumber= deque()
  dQueue = deque(inputNumber)
  for f in inputFunction:
    if f=='R':
      if reverse:
        reverse= False
      else:
        reverse= True
    elif f=='D':
      if dQueue:
       if reverse==True:
         dQueue.pop()
       else:
         dQueue.popleft()
      else:
        check=True
        print("error")
        break
  if(reverse==True and check==False):
    dQueue.reverse()
    print('['+ ",".join(dQueue) + ']')
  if(reverse==False and check==False):
    print('['+ ",".join(dQueue) + ']')
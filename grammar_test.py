import sys
input= sys.stdin.readline

K=int(input())
stack=[]
for i in range(K):
  test= int(input())
  if test==0:
    stack.pop()
  else:
    stack.append(test)
ans=0
for i in range(len(stack)):
  ans+=stack[i]
print(ans)
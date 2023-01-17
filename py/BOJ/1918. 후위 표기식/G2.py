#1918 후위 표기식
# infix to postfix
import sys
input = sys.stdin.readline

def infixToPostfix(infix):
  postfix= []
  notAlpha = [] # operator와 괄호를 담을 스택
  for step in infix:
    if step.isalpha(): #알파벳이라면 postfix에 바로 붙여줌
      postfix.append(step)
    else: # 알파벳이 아니면 괄호이거나 연산자
      if step == '(':
        notAlpha.append(step)
      elif step == ')':
        while len(notAlpha) != 0 and notAlpha[-1] != '(': # 여는 괄호 만날 때까지 push
          postfix.append(notAlpha.pop())
        notAlpha.pop() # 여는 괄호 제거
      elif step == '*' or step == '/': # 우선순위가 가장 높음
        while len(notAlpha) != 0 and (notAlpha[-1] == '*' or notAlpha[-1] =='/'):
          postfix.append(notAlpha.pop())
        notAlpha.append(step)
      elif step == '+' or step=='-':
        while len(notAlpha) != 0 and notAlpha[-1] != '(': # +,- 보다 우선순위가 크므로 postfix에 push
          postfix.append(notAlpha.pop())
        notAlpha.append(step)
  while len(notAlpha) != 0:
    postfix.append(notAlpha.pop())
  return postfix

input = input().rstrip()
answer = infixToPostfix(input)
print("".join(answer))

#1759. 암호 만들기
from sys import stdin
input = stdin.readline

def dfs(depth, password, idx):
  global vowelCount, consonantCount
  if depth == L and vowelCount >= 1 and consonantCount >= 2:
    for i in password:
      print(i, end='')
    print()  
    return
  for i in range(idx, C):
    if arr[i] in vowel:
      vowelCount+=1
    else:
      consonantCount+=1
    password.append(arr[i])
    dfs(depth+1, password, i+1)
    if arr[i] in vowel:
      vowelCount-=1
    else:
      consonantCount-=1
    password.pop()

# L = 암호는 서로 다른 L개의 알파벳 소문자
# C = C개의 문자
L, C = map(int, input().split())
arr = sorted(list(map(str, input().split())))
vowel = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0 #모음갯수 aeiou
consonantCount = 0 #자음갯수

dfs(0, [], 0)
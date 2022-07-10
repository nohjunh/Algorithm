x,y,w,h= map(int,input().split())

test1= w-x
test2= h-y
print(min(test1, test2, x, y))
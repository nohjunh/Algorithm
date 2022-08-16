import sys

N = int(sys.stdin.readline())
Nlist = []
often = []

for i in range(N):
    Nlist.append(int(sys.stdin.readline()))

print(round(sum(Nlist)/N)) #평균

Nlist.sort()

print(Nlist[int((N-1)/2)]) #중앙값

hashmap = {}
big = Nlist[0]
cnt = 0

for i in Nlist:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for i in range(-4000, 4001):
    if i in hashmap:
        hashmap[big] < hashmap[i]
        big = i

for i in range(-4000, 4001):
    if i in hashmap:
        if hashmap[big] == hashmap[i]:
            often.append(i)
            cnt+=1

often.sort()
print("~~~",  big)
#최빈값
if cnt==1:
    print(big)
else:
    print(often[0])

print(max(Nlist)-min(Nlist)) # 범위
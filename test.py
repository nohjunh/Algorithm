candidate, kim, lim = map(int, input().split())
count=0
while kim != lim:
    if kim %2 ==0:
        if kim//2 !=0:
            kim//=2
    else:
        if kim//2 !=0:
            kim//=2
            kim+=1

    if lim %2 ==0:
        if lim//2 !=0:
            lim//=2
    else:
        if lim//2 !=0:
            lim//=2
            lim+=1
    count+=1

print(count)
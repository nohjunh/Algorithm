def solve(num):
    global map

    if num==3:
        map[0][:3] = map[2][:3] = ["*"]*3
        map[1][:3] = ["*"," ","*"]
        return
    
    a= num//3
    solve(num//3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                map[a*i+k][a*j : a*(j+1)] = map[k][:a]
                

test_input= int(input())

map= [[" " for _ in range(test_input)] for _ in range(test_input)]

solve(test_input)

for i in map:
    print("".join(str(s) for s in i))

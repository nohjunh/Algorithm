A,B = map(int, input().split())

reverse_A= list(str(A))
reverse_A= reverse_A[::-1]
reverse_B= list(str(B))
reverse_B= reverse_B[::-1]
reverse_A= "".join(reverse_A)
reverse_B= "".join(reverse_B)

if int(reverse_B) > int(reverse_A):
    print(int(reverse_B))
else:
    print(int(reverse_A))
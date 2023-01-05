test_input= list(map(int, input().split()))

sorted_input= sorted(test_input)
sorted_input_reverse= sorted(test_input, reverse=True)

if test_input == sorted_input:
    print("ascending")
elif test_input == sorted_input_reverse:
    print("descending")
else:
    print("mixed")
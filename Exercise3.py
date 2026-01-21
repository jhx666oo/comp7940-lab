def print_factor(x):
    print(f"Factors of {x}:")
    for i in range(2, x):
        if x % i == 0:
            print(i)

l = [52633, 8137, 1024, 999]
for number in l:
    print_factor(number)
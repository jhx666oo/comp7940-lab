def print_factor(x):
    print(f"Factors of {x}:")
    for i in range(2, x):
        if x % i == 0:
            print(i)
if __name__ == '__main__':
    x = 52633
    print_factor(x)
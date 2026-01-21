# Lab 1: Python Basic Exercises

# Part 1: Hello World (Instruction 5)
def main():
    print("Hello World")

# Exercise 1 & 2: Factors Function (Instruction 9)
def print_factor(x):
    """Prints all factors of the given parameter x"""
    print(f"Factors of {x}:")
    for i in range(1, x + 1):  # Include 1 and x itself
        if x % i == 0:
            print(i)

if __name__ == '__main__':
    main()
    
    # Exercise 1: Finding factors of 52633
    x = 52633
    print_factor(x)
    
    # Exercise 3: List Iteration
    print("\n--- Exercise 3: List Iteration ---")
    l = [52633, 8137, 1024, 999]
    for num in l:
        print_factor(num)
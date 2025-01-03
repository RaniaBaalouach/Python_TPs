def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

n = int(input("Enter a number: "))
print(f"Factorial (using for loop): {factorial_for(n)}")
print(f"Factorial (using while loop): {factorial_while(n)}")

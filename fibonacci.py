def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage:
num_terms = int(input("Enter the number of terms: "))
result = fibonacci(num_terms)
print("Fibonacci sequence:", result)



def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example: Print first n Fibonacci numbers
num_terms = int(input("Enter the number of terms: "))
for i in range(num_terms):
    print(fibonacci_recursive(i), end=' ')
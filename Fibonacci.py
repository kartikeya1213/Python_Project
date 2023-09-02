
def fibonacci(n):
    fib_series = []
    a, b = 0, 1

    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci(num_terms)
    print("Fibonacci series:")
    print(result)

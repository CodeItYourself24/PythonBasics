# fibonacci series for a range of numbers

def fibonacci(n):
    a, b = 0, 1
    fibonacci_series = []
    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Generating the first 10 numbers in the Fibonacci series
result = fibonacci(10)
print(result)
def countdown(i):
    print("Отсчет:", i)
    if i <= 1:
        return
    countdown(i-1)

countdown(10)

def factorial_recursion(n):
    if n <= 0:
        raise ValueError("Cannot be zero or negative")
    if n == 1:
        return 1
    return n * factorial_recursion(n-1)

n = 5
print(f"Факториал {n}: {factorial_recursion(n)}")

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = 7
print(f"{n}-ое число Фибоначчи: {fibonacci(n)}")
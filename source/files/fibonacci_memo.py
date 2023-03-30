memo = {}

def fibonacci(n: int) -> int:
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        memo[n] = value
        return value

print(fibonacci(80))
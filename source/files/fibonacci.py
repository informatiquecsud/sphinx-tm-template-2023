memo = {}

def fib(n: int) -> int:
    if n in [0, 1]:
        return 1
    elif n in memo:
        return memo[n]
    else:
        value = fib(n - 1) + fib(n - 2)
        memo[n] = value
        return value
         
print(fib(80))
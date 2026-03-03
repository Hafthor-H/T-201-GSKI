

def fibonacci(num: int) -> int:
    if num == 0 or num == 1:
        return num
    
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(10))
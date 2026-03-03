

def factorial(num: int) -> int:
    assert num >= 0, "No negative numbers"

    if num == 0:
        return 1
    
    return num * factorial(num - 1)

print(factorial(5))
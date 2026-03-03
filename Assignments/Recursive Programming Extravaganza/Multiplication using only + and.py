

def multiply(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    if a < 0 and b < 0:
        a, b = abs(a), abs(b)

    if b < 0:
        return b + multiply(a-1 ,b)

    return a + multiply(a,b-1)


print(multiply(-4,-2))
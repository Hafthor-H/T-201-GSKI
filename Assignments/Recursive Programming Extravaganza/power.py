

def power(base: int, exp: int) -> int:
    assert base >= 0, "Must be a non negative integer"
    if base == 1:
        return 1
    if exp == 0:
        return 1
    
    print("-"*30)
    return base * power(base, exp-1)

print(power(6,3))
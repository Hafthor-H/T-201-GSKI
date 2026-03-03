

def sum_of_digits(num: int) -> int:
    if num == 0:
        return 0

    last_digit = num % 10
    new = num // 10

    return last_digit + sum_of_digits(new)

print(sum_of_digits(11))
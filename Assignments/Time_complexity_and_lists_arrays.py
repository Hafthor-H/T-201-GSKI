#https://stackoverflow.com/questions/66252928/how-to-determine-if-my-code-is-on-onlogn-o1-on2

def power(num_a: int, num_b: int) -> int:
    #Time complexity: O(1)
    return num_a**num_b

def multiply_two_num(num_a: int, num_b) -> int:
    #Time complexity: O(n)
    summa = 0
    for _ in range(num_a):
        summa += num_b
    return summa

multiply_two_num(8,8)

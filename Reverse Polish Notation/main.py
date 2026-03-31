
def main():
    vars = {}
    stack = []
    operators = []

    while True:
        expr = input().split(" ")

        if "=" in expr:
            if len(expr) > 3:
                print("ERROROR")
                continue
            vars[expr[0]] = int(expr[2])
            continue
        else:
            break

    for i in expr:
        if i in "+-/*":
            operators.append(i)
        else:
            try:
                stack.append(int(i))
            except:
                stack.append(vars[i.lower()])

    for op in operators:

        if op == "+":
            num_2 = stack.pop(1)
            stack[0] += num_2

        elif op == "-":
            num_2 = stack.pop(1)
            stack[0] -= num_2

        elif op == "/":
            num_2 = stack.pop(1)
            stack[0] /= num_2
            
        elif op == "*":
            num_2 = stack.pop(1)
            stack[0] *= num_2
    print(stack[0])
main()
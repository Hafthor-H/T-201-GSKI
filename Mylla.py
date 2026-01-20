def check_straight(line:list) -> bool:
    if "_" in line:
        return False
    elif len(set(line)) == 1 and line[0] == "O":
        return True
    return False

def check_diagonal(line_1: list, line_2: list, line_3: list) -> bool:
    if line_1[0] == "O" and line_2[1] == "O" and line_3[2] == "O":
        return True
    elif line_1[2] == "O" and line_2[1] == "O" and line_3[0] == "O":
        return True
    return False

def check_vertical(line_1: list, line_2: list, line_3: list) -> bool:
    if line_1[0] == "O" and line_2[0] == "O" and line_3[0] == "O":
        return True
    elif line_1[1] == "O" and line_2[1] == "O" and line_3[1] == "O":
        return True
    elif line_1[2] == "O" and line_2[2] == "O" and line_3[2] == "O":
        return True
    return False
def main():
    line_1: list = list(input())
    straight_1 = check_straight(line_1)
    line_2: list = list(input())
    straight_2 = check_straight(line_2)
    line_3: list = list(input())
    straight_3: bool = check_straight(line_3)
    diagonal: bool = check_diagonal(line_1, line_2, line_3)
    vertical: bool = check_vertical(line_1,line_2,line_3)
    if (straight_1 + straight_2 + straight_3 + diagonal + vertical) < 1:
        print("Neibb")
    else:
        print("Jebb")
main()
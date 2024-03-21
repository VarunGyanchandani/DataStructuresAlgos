def check_valid_parenth(s, string):
    count = 0
    for char in string:
        if char == '(':
            s.append(char)
        elif s and char == ')':
            count += 1
            s.pop()
    return count


if __name__ == "__main__":
    stack = []
    string = "())(())())("
    print(check_valid_parenth(stack, string))

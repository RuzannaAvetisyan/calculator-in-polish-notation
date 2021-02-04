INT = ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
FLOAT = ('-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
#OPERATION = ('add:', '+', 'sub:', '-', 'mul:', '*', 'div:', '/')
OPERATION = ('+', '-', '*', '/')


def check_int(s):
    for i in s:
        if i not in INT:
            return False
    if s.__contains__('-'):
        if s.count('-') > 1 or s.index('-') != 0:
            return False
    return True


def check_float(s):
    for i in s:
        if i not in FLOAT:
            return False
    if s.__contains__('-'):
        if s.count('-') > 1 or s.index('-') != 0:
            return False
    if s.__contains__('.'):
        if s.count('.') != 1 or s.index('.') == len(s)-1 or \
                (s.index('.') == 1 and s[0] == '-') or s.index('.') == 0:
            return False
    return True


def calculator(expression):
    if expression[0] == '+':
        print(f'Result: {expression[1]+expression[2]}')
    elif expression[0] == '-':
        print(f'Result: {expression[1] - expression[2]}')
    elif expression[0] == '*':
        print(f'Result: {expression[1] * expression[2]}')
    else:
        if expression[2] == 0:
            print("Zero division error")
        else:
            print(f'Result: {expression[1]/expression[2]}')


def error_massage():
    print("ERROR: Invalid expression")


if __name__ == '__main__':
    while True:
        count_err_number = 0
        expression = input("Expression: ").split()
        if len(expression) == 3:
            if expression[0] in OPERATION:
                for i in (1, 2):
                    if len(expression[i]) > 0:
                        if check_int(expression[i]):
                            expression[i] = int(expression[i])
                        elif check_float(expression[i]):
                            expression[i] = float(expression[i])
                        else:
                            count_err_number = count_err_number + 1
                if count_err_number == 0:
                    calculator(expression)
                else:
                    error_massage()
            else:
                error_massage()
        else:
            error_massage()


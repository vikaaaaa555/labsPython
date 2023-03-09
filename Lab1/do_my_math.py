from consts import CONST

def do_math(val1, val2, operator):
    if operator == CONST[0]:
        return val1 + val2

    elif operator == CONST[1]:
        return val1 - val2

    elif operator == CONST[2]:
        return val1 * val2

    elif operator == CONST[3]:
        return val1 / val2

    else:
        print("Недопустимое значение")
import consts
import main

def do_math(val1, val2, operator):
    match main.operator == consts.const:
        case (add,_):
            result = val1 + val2
            return result

        case (_,sub):
            result = val1 - val2
            return result

        case (_,_,mul):
            result = val1 * val2
            return result

        case (_,_,_,div):
            result = val1 / val2
            return result
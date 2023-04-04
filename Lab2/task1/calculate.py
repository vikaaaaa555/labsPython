import re

def calc_sentence(msg:str) -> int:
    reg = r'[.?!]+'
    return len(re.findall(reg, msg))

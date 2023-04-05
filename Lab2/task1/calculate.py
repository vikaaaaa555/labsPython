import re


def all_calc_sentences(txt: str) -> int:
    reg = r'[.?!]+'
    return len(re.findall(reg, txt))


def non_declarative_sentences(txt: str) -> int:
    reg = r'[!?]+'
    return len(re.findall(reg, txt))


def count_words(txt: str) -> int:
    reg = r'[\w-]+'
    return len(re.findall(reg, txt))


def average_length_of_sentence(txt: str) -> int:
    return count_words(txt) / all_calc_sentences(txt)

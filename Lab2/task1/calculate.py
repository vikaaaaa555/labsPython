import constans
import re


def all_sentences(txt: str) -> int:
    return len(re.findall(constans.ALL_SENTENCES, txt))
#все предложения


def calc_non_declarative_sentences(txt: str) -> int:
    return len(re.findall(constans.NON_DECLARATIVE_SENTENCES, txt))
#неповествовательные


def count_words(txt: str) -> int:
    return len(re.findall(constans.WORDS, txt))
#количество слов


def average_length_of_sentence(txt: str) -> int:
    return round(count_characters(txt) / all_sentences(txt))
#средняя длина предложения


def average_lenght_of_words(txt: str) -> int:
    return round(count_characters(txt) / count_words(txt))
#средняя длина слова


def delete_numbers(txt: str) -> str:
    return re.sub(constans.NUMBERS, ' ', txt)
#удалить числа


def count_characters(txt: str) -> int:
    new_txt = delete_numbers(txt)

    return len(re.findall(constans.CHARACTERS, new_txt))
#количество символов



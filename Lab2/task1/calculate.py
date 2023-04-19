import collections
import constans
import re


def all_sentences(txt: str) -> int:
    sentences = len(re.findall(constans.ALL_SENTENCES_PATTERN, txt))

    for i in constans.ONE_LETTERS_ABBRIVATION:
        sentences -= txt.count(i)

    for i in constans.FEW_LETTERS_ABBRIVATION:
        sentences -= txt.count(i)

    return sentences
    # все предложения


def calc_non_declarative_sentences(txt: str) -> int:
    return len(re.findall(constans.NON_DECLARATIVE_SENTENCES_PATTERN, txt))
    # неповествовательные


def count_words(txt: str) -> int:
    return len(re.findall(constans.WORDS_PATTERN, txt))
    # количество слов


def average_length_of_sentence(txt: str) -> int:
    if all_sentences(txt) == 0:
        return 0
    else:
        return round(count_characters(txt) / all_sentences(txt))
    # средняя длина предложения


def average_length_of_words(txt: str) -> int:
    if all_sentences(txt) == 0:
        return 0
    else:
        return round(count_characters(txt) / count_words(txt))
    # средняя длина слова


def delete_numbers(txt: str) -> str:
    return re.sub(constans.NUMBERS_PATTERN, ' ', txt)
    # удалить числа


def count_characters(txt: str) -> int:
    new_txt = delete_numbers(txt)

    return len(re.findall(constans.CHARACTERS_PATTERN, new_txt))
    # количество символов


def get_top_ngrams(txt, n = 4, k = 10) -> str:
    txt = re.sub(constans.PATTERN_FOR_NGRAMS, '', txt).lower()
    words = txt.split()

    ngrams = (tuple(words[i:i + n]) for i in range(len(words) - n + 1))
    top_ngrams = collections.Counter(ngrams).most_common(k)

    return str(top_ngrams)
    # n-grams

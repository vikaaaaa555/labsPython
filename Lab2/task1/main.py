import calculate
import constans


def main():
    text = input("Input some text: ")

    print("Amount of sentences in the text: ", calculate.all_sentences(text))
    print("Amount of non-declarative sentences in the text: ",
        calculate.calc_non_declarative_sentences(text))
    print("Average length of the sentence in characters: ",
        calculate.average_length_of_sentence(text))
    print("Average length of the word in the text in characters: ",
        calculate.average_length_of_words(text))


    try:
        n, k = map(int, input("Enter n and k with a space: ").split())
    except ValueError:
        print("Invalid value!")
        exit()

    print(calculate.get_top_ngrams(text, n, k))


if __name__ == "__main__":
    main()

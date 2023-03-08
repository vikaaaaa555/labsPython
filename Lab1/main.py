from hello import hello_world
from do_my_math import do_math
from even_numbers import find_even


def main():

    hello_world()

    try:
        x, y = map(int, input("Введите 2 числа через пробел: ").split())
    except ValueError:
        print("Недопустимое значение")
        exit()

    operator = input("Введите оператор (add, sub, mul или div): ")
    print(do_math(x, y, operator))

    print(find_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if __name__ == '__main__':
    main()

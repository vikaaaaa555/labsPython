def find_even(my_list: list) -> list:
    return list(filter(lambda x: not int(x) % 2, my_list))
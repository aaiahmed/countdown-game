from numbers_game import find_solution, get_numbers
from letters_game import get_permutations, in_dictionary, get_letters, \
    get_words, get_valid_english_words


if __name__ == '__main__':
    # string = 'optimums'
    # valid_words = sorted([x for x in get_permutations(string) if in_dictionary(x)], key=lambda s: len(s), reverse=True)
    # print(valid_words[0:4])
    #
    target = "404"
    numbers = [100, 10, 2, 9, 2, 1]
    print(find_solution(numbers, target)[0:2])

    # string = "OUIGREQF"
    # for item in get_valid_english_words(string).items():
    #     print(item[0], item[1])

    # numbers = get_numbers(0)
    # print(numbers)





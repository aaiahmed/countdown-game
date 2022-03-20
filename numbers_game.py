import json
import random
NUMBERS_LOOKUP_FILE = 'math_lookup.json'
NUMBER_OF_SOLUTIONS = 1
BIG_NUMBERS = [25, 50, 75, 100]
SMALL_NUMBERS = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
TOTAL_NUMBERS = 6


def get_numbers(big: int) -> list:
    return random.sample(BIG_NUMBERS, big) + random.sample(SMALL_NUMBERS, TOTAL_NUMBERS - big)


def get_target() -> int:
    return random.randint(100, 999)


def read_lookup() -> dict:
    with open(NUMBERS_LOOKUP_FILE) as f:
        return json.loads(f.read())


def find_solution(numbers: list, target: int) -> list:
    answer = []
    lookup_dict = read_lookup()
    solutions = lookup_dict[str(target)]
    for solution in solutions:
        if all(x in numbers for x in solution[0]):
            answer.append(solution[1])
        if len(answer) == NUMBER_OF_SOLUTIONS:
            break
    return answer

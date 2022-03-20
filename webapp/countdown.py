from flask import Blueprint, render_template, request
from letters_game import get_letters, get_valid_english_words
from numbers_game import get_numbers, get_target, find_solution
from threading import Thread

bp = Blueprint('countdown', __name__)
cache = {}


def reset_numbers():
    cache['numbers'] = ""
    cache["target"] = ""
    cache["solution"] = ""


def reset_letters():
    cache['letters'] = ""
    cache["word1"] = ""
    cache["word2"] = ""
    cache["word3"] = ""


def generate_letters():
    reset_letters()
    reset_numbers()
    vowels = int(request.form["vowels"]) if request.form["vowels"] != "" else 4
    consonants = int(request.form["consonants"]) if request.form["consonants"] else 5
    cache['letters'] = ' '.join(get_letters(vowels, consonants))


def get_letters_solution():
    if cache["word1"] == "":
        letters = ''.join(cache.get('letters').split(' '))
        valid_words = get_valid_english_words(letters)
        cache["word1"] = f"{valid_words[0][0]}: {valid_words[0][1]}"
        cache["word2"] = f"{valid_words[1][0]}: {valid_words[1][1]}"
        cache["word3"] = f"{valid_words[2][0]}: {valid_words[2][1]}"
        reset_numbers()


def generate_numbers(big: int):
    reset_letters()
    reset_numbers()
    cache['numbers'] = ' '.join([str(x) for x in get_numbers(big)])


def get_numbers_target():
    cache['target'] = str(get_target())
    reset_letters()


def get_numbers_solution():
    if cache["solution"] == "":
        numbers = [int(x) for x in cache["numbers"].split(' ')]
        print('**')
        solution = find_solution(numbers=numbers, target=cache["target"])[0]
        if solution != "":
            cache['solution'] = solution
        reset_letters()


@bp.route('/countdown', methods=['GET', 'POST'])
def countdown():
    if request.method == 'POST':
        if request.form.get("generate"):
            generate_letters()
            Thread(target=get_letters_solution).start()
        elif request.form.get("solution_letters"):
            get_letters_solution()
        elif request.form.get("one_big"):
            generate_numbers(big=1)
        elif request.form.get("two_big"):
            generate_numbers(big=2)
        elif request.form.get("three_big"):
            generate_numbers(big=3)
        elif request.form.get("four_big"):
            generate_numbers(big=4)
        elif request.form.get("six_small"):
            generate_numbers(big=0)
        elif request.form.get("target"):
            get_numbers_target()
            Thread(target=get_numbers_solution).start()
        elif request.form.get("solution_numbers"):
            get_numbers_solution()
    else:
        reset_letters()
        reset_numbers()
    return render_template('countdown.html',
                           letters=cache.get('letters'),
                           word1=cache.get('word1'),
                           word2=cache.get('word2'),
                           word3=cache.get('word3'),
                           numbers=cache.get('numbers'),
                           target=cache.get('target'),
                           solution=cache.get("solution"))

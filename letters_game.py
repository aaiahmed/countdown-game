import itertools
import random
import requests
import json

from nltk.corpus import words

ENGLISH_WORDS = set(words.words())
VOWELS = ["A", "E", "I", "O", "U"]
CONSONANTS = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
              "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
DICTIONARY_API = "https://api.dictionaryapi.dev/api/v2/entries/en/"
NUMBER_OF_SOLUTIONS = 3


def get_letters(vowels: int, consonants: int) -> list:
    letters = random.sample(VOWELS, vowels) + random.sample(CONSONANTS, consonants)
    random.shuffle(letters)
    return letters


def get_permutations(string: str) -> set:
    chars = list(string)
    perms = []
    for x in range(2, len(string)):
        perms = perms + [''.join(x) for x in itertools.permutations(chars, x)]
    return set(perms)


def in_dictionary(word: str) -> bool:
    return word in ENGLISH_WORDS


def get_words(string: str) -> list:
    return sorted([x for x in get_permutations(string.lower()) if in_dictionary(x)], key=lambda s: len(s), reverse=True)


def get_valid_english_words(string: str) -> list:
    valid_words = []
    words = get_words(string)
    for word in words:
        url = f"{DICTIONARY_API}{word}"
        request = requests.get(url)
        response = json.loads(request.text)
        try:
            meaning = response[0].get("meanings")[0].get("definitions")[0].get("definition")
            valid_words.append([word, meaning])
        except KeyError:
            print(word + " is not a valid English word, skipping...")
        if(len(valid_words)) == NUMBER_OF_SOLUTIONS:
            break
    return valid_words


def download_words():
    import nltk
    nltk.download('words')

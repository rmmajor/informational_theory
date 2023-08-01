import random
import string


def lz78_encode(input_string: str) -> tuple[list[tuple[int, str]], dict]:
    dictionary: dict[str, int] = {'': 0}
    codes: list[tuple[int, str]] = []
    phrase: str = ''
    index: int = 1

    for c in input_string:
        if phrase + c in dictionary:  
            phrase += c  
        else:
            codes.append((dictionary[phrase], c))
            dictionary[phrase + c] = index
            phrase = ''
            index += 1

    if phrase != '': 
        codes.append((dictionary[phrase], ''))
        dictionary[phrase + '(eof)'] = index

    return codes, dictionary


def make_encoded_str_from_codes(codes: list[tuple[int, str]]):
    encoded_str: str = ""
    for code in codes:
        index, letter = code
        encoded_str += str(index) + letter

    return encoded_str


def calculate_avg_len_of_the_code_phrase(codes):
    total_len = 0
    for index, phrase in codes:
        bin_phrase = "{0:b}".format(index) + string_to_binary(phrase)
        total_len += len(bin_phrase)

    return total_len / len(codes)


def string_to_binary(s):
    ascii_codes = [ord(c) for c in s]
    binary_string = "".join(format(code, "08b") for code in ascii_codes)
    return binary_string


def encoded_string_to_binary(codes: list[tuple]):
    output_string = ''
    for key, value in codes:
        output_string += "{0:b}".format(key) + string_to_binary(value)

    return output_string


def generate_words_sequence():
    num_words: int = random.randint(20, 30)
    text: str = ''

    for i in range(num_words):
        word_length: int = random.randint(3, 8)
        word: str = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        text += word + ' '

    return text.strip()


def do_task(input_string: str):
    print("Довжина вхідної строки", len(input_string))
    codes, dictionary = lz78_encode(input_string)
    print("Коди:", codes)
    dict_to_print = [(index, phrase) for phrase, index in dictionary.items()]
    print("Словник:", dict_to_print)
    print("Довжина словника", len(dict_to_print))
    print("Кодована послідовність", make_encoded_str_from_codes(codes))
    print("Кодована послідовність (бінарна)", encoded_string_to_binary(codes))
    print("Середня довжина кодової фрази:", calculate_avg_len_of_the_code_phrase(codes))


if __name__ == '__main__':
    # input_string = 'sir_sid_eastman_easily_teases_sea_sick_seals'

    # завдання а
    print()
    input_string = str(input("Введіть власне прізвище: "))
    input_string += input_string
    print(input_string)
    do_task(input_string)

    # завдання б
    print()
    input_string = str(input("Ввід довільного фрагмента тексту довжиною від 20 до 30 слів: "))
    do_task(input_string)

    # завдання в
    print()
    print("Генерую фрагмент тексту довжиною від 20 до 30 слів: ")
    text = generate_words_sequence()
    print(text)
    do_task(text)

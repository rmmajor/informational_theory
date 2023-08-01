import math

import numpy as np
import matplotlib.pyplot as plt


def float_dec_to_bin_convert(float_number, precision=5):
    int_part, dec_part = str(float_number).split(".")
    int_part = int(int_part)
    dec_part = int(dec_part)
    res = bin(int_part).lstrip("0b") + "."
    for x in range(precision):
        nxt = int_to_float(dec_part) * 2
        try:
            int_part, dec_part = str(nxt).split(".")
        except:
            res += '0'
            continue

        dec_part = int(dec_part)
        res += int_part

    if res[0] == '.':
        res = '0' + res

    return res


def int_to_float(num):
    """
    Хз як це назвати, кароче функ приймає 123 і робить 0.123
    """
    while num > 1:
        num /= 10
    return num


class ShennonCodes:

    def __init__(self, name: str = '') -> None:
        self.name: str = name
        self.F: list[float] = []
        self._F: list[float] = []
        self._F_bin: list[str] = []
        self.lens_of_codes: list[int] = []
        self.freq_table: dict[str, int | float] = {}
        self.distribution: list[float] = []
        self.codes: dict[str, str] = {}
        self.expected_length: float = 0
        self.entropy: float = 0
        self.encoded_name: str = ""

    def build_freq_table(self) -> None:
        for char in self.name:
            if char not in self.freq_table:
                self.freq_table[char] = 0
            self.freq_table[char] += 1

    def build_distribution(self) -> None:
        total_cnt: int = sum(self.freq_table.values())
        for key in self.freq_table:
            self.distribution.append(self.freq_table[key] / total_cnt)

    def _build_mock_freq_table(self):
        keys_list = ['x' + str(i) for i in range(1, len(self.distribution)+1)]
        self.freq_table.fromkeys(keys_list)
        for key, value in zip(keys_list, self.distribution):
            self.freq_table[key] = value

    def set_distribution(self, distribution: list[float]) -> None:
        """Коли лабу треба робити на росподілі, а не на строці"""
        self.distribution = distribution
        self._build_mock_freq_table()
        print("Розводіл:", self.distribution)

    def gen_F(self) -> None:
        self.F = np.cumsum(self.distribution)
        print('F(x)', self.F)

    def gen__F(self) -> None:
        self._F = self.F + -0.5 * np.array(self.distribution)
        print('_F(x)', self._F)

    def _F_to_bin(self, precision: int = 8) -> None:
        for _f in self._F:
            _f_bin = float_dec_to_bin_convert(_f, precision)
            self._F_bin.append(_f_bin)
        print("_F(x) бінарне", self._F_bin)

    def calculate_lens_of_codes(self) -> None:
        self.lens_of_codes = np.ceil(np.log2(1 / np.array(self.distribution))).astype(int) + 1
        print("Довжини кодів", self.lens_of_codes)

    def calculate_codes(self) -> None:
        print("codes: ", end='')
        for char, _f_bin, l in zip(self.freq_table, self._F_bin, self.lens_of_codes):
            self.codes[char] = _f_bin[2:l + 2]
            # print(_f_bin[2:l + 2])
        print(self.codes)

    def plot_F(self) -> None:
        cumulative_probabilities = list(self.F)
        cumulative_probabilities.insert(0, 0)

        plt.plot(cumulative_probabilities, drawstyle='steps-post', color='black')
        plt.scatter(
            x=[i for i in range(1, len(self.F)+1)],
            y=self._F,
            color='blue'
        )

        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.show()

    def check_kraft_inequality(self) -> bool:
        """
        Нерівність Крафта стверджує, що для будь-якої послідовності неперетинаючихся кодових
        слів довжинами l1, l2, ..., ln і алфавіту розміру r, де li - довжина i-го
        кодового слова, має місце нерівність:

            1/r^(l1) + 1/r^(l2) + ... + 1/r^(ln) <= 1
        :return: True of False
        """
        r = 2  # алфавіт має розмір 2 (0 та 1)
        sum = 0
        for length in self.lens_of_codes:
            sum += 1 / (r ** length)

        print(f"{sum} <= 1")
        return sum <= 1

    def calculate_entropy_of_dist(self) -> float:
        entropy: float = 0

        for p in self.distribution:
            entropy += -1 * p * math.log2(p)

        self.entropy = entropy
        return entropy

    def calculate_expected_len(self) -> float:
        expected_length: int = 0
        for p, code_len in zip(self.distribution, self.lens_of_codes):
            expected_length += p * code_len

        self.expected_length = expected_length
        return expected_length

    def encode_str(self) -> str:
        encoded_name = ""
        for char in self.name:
            encoded_name += self.codes[char]

        self.encoded_name = encoded_name
        return encoded_name


def make_lab_for_str(name):
    codes = ShennonCodes(name=name)
    codes.build_freq_table()
    print("Кількість входжень кожного символу в послідовність:", codes.freq_table)
    codes.build_distribution()

    codes.gen_F()
    codes.gen__F()
    codes.calculate_lens_of_codes()
    codes._F_to_bin()
    codes.calculate_codes()
    codes.plot_F()

    print()
    print("Нерівність Крафта")
    if codes.check_kraft_inequality():
        print("Нерівність виконується")
    else:
        print("Нерівність не виконується")

    print()
    print("Ентропія вихідного повідомлення:", codes.calculate_entropy_of_dist())
    print("Очікувана довжина вихідного повідомлення:", codes.calculate_expected_len())

    print("Закодована строка:", codes.encode_str())


def make_lab_for_dist(dist):
    codes = ShennonCodes()
    codes.set_distribution(dist)
    codes.gen_F()
    codes.gen__F()
    codes.calculate_lens_of_codes()
    codes._F_to_bin()
    codes.calculate_codes()
    codes.plot_F()

    print()
    print("Нерівність Крафта")
    if codes.check_kraft_inequality():
        print("Нерівність виконується")
    else:
        print("Нерівність не виконується")

    print()
    print("Ентропія розподілу:", codes.calculate_entropy_of_dist())
    print("Очікувана довжина послідовності:", codes.calculate_expected_len())


if __name__ == '__main__':
    name: str = "Майор Роман Юрійович"
    dist: list[float] = [0.11, 0.08, 0.13, 0.06, 0.06, 0.11, 0.11, 0.09, 0.11, 0.13]

    make_lab_for_str(name)
    print()
    print()
    print('=====================================================================================================')
    print()
    print()
    make_lab_for_dist(dist)

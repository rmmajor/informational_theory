import math
import random
from decimal import Decimal, getcontext

getcontext().prec = 31


class ArithmeticCodes:
    def __init__(self, name: str):
        self._l = None
        self.name: str = name
        self.freq_table: dict[str, int] = {}
        self.p_table: dict[str, Decimal] = {}
        self.intervals: dict[str, (Decimal, Decimal)] = {}
        self.code: Decimal = Decimal('0.0')
        self.decoded_name: str = ""
        self.bin_code: str = ""

        self.build_freq_table()
        self.build_p_table()
        self.build_intervals()

    def build_freq_table(self) -> dict[str, int]:
        for char in self.name:
            if char not in self.freq_table:
                self.freq_table[char] = 0
            self.freq_table[char] += 1

        return self.freq_table

    def build_p_table(self) -> dict[str, Decimal]:
        total_cnt = sum(self.freq_table.values())
        for key in self.freq_table:
            self.p_table[key] = Decimal(str(self.freq_table[key] / total_cnt))

        return self.p_table

    def build_intervals(self) -> dict[str, (Decimal, Decimal)]:
        low = Decimal('0.0')
        for c, p in self.p_table.items():
            high = low + p
            self.intervals[c] = (low, high)
            low = high
        return self.intervals

    def encode(self) -> Decimal:
        low, high = Decimal('0.0'), Decimal('1.0')
        for c in self.name:
            # Обчислення нових границь діапазону
            new_low = low + (high - low) * self.intervals[c][0]
            new_high = low + (high - low) * self.intervals[c][1]
            low, high = new_low, new_high
            print(c, low, high)

        self.code = low
        return self.code

    def decode(self) -> str:
        decoded_symbols: list[str] = []
        while len(decoded_symbols) < len(self.name):
            # Пошук символу, що відповідає діапазону
            for c, interval in self.intervals.items():
                if interval[0] <= self.code < interval[1]:
                    decoded_symbols.append(c)

                    # Обчислення нових границь діапазону
                    print(self.code, c, interval[0], interval[1])
                    self.code = (self.code - interval[0]) / (interval[1] - interval[0])
                    break

        # Повернення розкодованого рядка
        self.decoded_name = ''.join(decoded_symbols)
        return self.decoded_name

    def code_to_bin(self) -> str:
        dec_part = int(str(self.code)[2:])
        bin_dec_part = bin(dec_part)
        self.bin_code = bin_dec_part[2:]
        return bin_dec_part[2:]

    def l(self):
        self._l = math.ceil(math.log2(1 / self.code)) + 1
        print("l(x) =", self._l)
        return float(self.code) + (2 ** -self._l)


def generate_string(probabilities: list[float], length: int):
    symbols = "abcdefghijklmnopqrstuvwxyz"[:len(probabilities)]
    string = ''.join(random.choices(symbols, weights=probabilities, k=length))
    return string


def make_lab(s: str):
    code = ArithmeticCodes(name=s)
    print("Кількість входжень символів в рядок:", code.freq_table)
    print("Частоти входжень символів в рядок:", code.p_table)
    print("Вхідна таблиця для послідовності:", code.intervals)

    print("Таблиця кодування")
    print("Код послідовності:", code.encode())
    print("новий код", code.l())
    print("Бінарний код послідовності:", code.code_to_bin())

    print("Таблиця декодування")
    print("Декодована стрічка:", code.decode())
    print("Чи співпадають вхідна і декодована стрічки:", s == code.decoded_name)


def main():
    print()
    print("Для послідовності '5'")
    dist = [0.06, 0.13, 0.08, 0.13, 0.10, 0.07, 0.10, 0.14, 0.09, 0.09]

    s = generate_string(dist, 5)
    print("Вхідна стрічка:", s)
    make_lab(s)

    print()
    print("Для послідовності '10'")
    s = generate_string(dist, 10)
    print("Вхідна стрічка:", s)
    make_lab(s)

    print()
    print("Для ПІБ")
    name = 'Майор Роман Юрійович'
    make_lab(name)


if __name__ == '__main__':
    main()

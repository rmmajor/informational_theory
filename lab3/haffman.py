import heapq
import math


class Node:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanTree:
    def __init__(self, name=''):
        self.name = name
        self.root = None
        self.codes = {}
        self.code_lens = {}
        self.freq_table = {}
        self.p_table = {}
        self.encoded_name = ""
        self.entropy = None
        self.expected_length = None

    def build_freq_table(self):
        for char in self.name:
            if char not in self.freq_table:
                self.freq_table[char] = 0
            self.freq_table[char] += 1

    def build_p_table(self):
        total_cnt = sum(self.freq_table.values())
        for key in self.freq_table:
            self.p_table[key] = self.freq_table[key] / total_cnt

    def build_freq_table_distribution(self, dist):
        """
        костиль для побудови дерева з готовими імовірностями
        """
        keys_list = ['x'+str(i) for i in range(len(dist))]
        print(keys_list)
        self.freq_table.fromkeys(keys_list)
        for key, value in enumerate(dist):
            self.freq_table[key] = value

    def build_tree(self):
        nodes = [Node(char, freq) for char, freq in self.freq_table.items()]
        heapq.heapify(nodes)
        while len(nodes) > 1:
            left_node = heapq.heappop(nodes)
            right_node = heapq.heappop(nodes)
            merged_node = Node(left=left_node, right=right_node, freq=left_node.freq + right_node.freq)
            heapq.heappush(nodes, merged_node)
        self.root = nodes[0]

    def build_codes(self):
        def dfs(node, code=""):
            if node:
                if node.is_leaf():
                    self.codes[node.char] = code
                    self.code_lens[node.char] = len(code)
                dfs(node.left, code + "0")
                dfs(node.right, code + "1")

        dfs(self.root)

    def encode(self):
        encoded_name = ""
        for char in self.name:
            encoded_name += self.codes[char]
        self.encoded_name = encoded_name
        return encoded_name

    def decode(self, encoded_name):
        decoded_name = ""
        current_node = self.root
        for bit in encoded_name:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.is_leaf():
                decoded_name += current_node.char
                current_node = self.root
        return decoded_name

    def draw_tree(self):
        def draw(node, level=0, char='  '):
            if node.is_leaf():
                print(' ' * 6 * level + char * 3 + str(node.freq) + ' {' + str(node.char) + '}')
                return

            draw(node.right, level=level+1)
            print(' ' * 6 * level + char * 3 + str(node.freq))
            draw(node.left, level=level + 1)

        draw(self.root)

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
        for key in self.code_lens:
            sum += 1 / (r ** self.code_lens[key])

        print(f"{sum} <= 1")
        return sum <= 1

    def calculate_entropy_of_dist(self) -> float:
        entropy: float = 0
        p = self.p_table

        for key in p:
            entropy += -1 * p[key] * math.log2(p[key])

        self.entropy = entropy
        return entropy

    def calculate_expected_len(self) -> int:
        expected_length: int = 0
        for key in self.p_table:
            expected_length += self.p_table[key] * self.code_lens[key]

        self.expected_length = expected_length
        return expected_length


def make_lab_for_str(name):
    print("Довжина послідовності:", len(name))

    tree = HuffmanTree(name)
    tree.build_freq_table()
    tree.build_p_table()
    tree.build_tree()
    tree.build_codes()

    print("Кількість входжень кожного символу в послідовність:", tree.freq_table)
    print("Імовірність появи кожного символу в послідовності:", tree.p_table)
    print("Кодові слова:", tree.codes)
    print("Довжини кодових слів:", tree.code_lens)

    tree.draw_tree()

    encoded_name = tree.encode()
    print(encoded_name)
    decoded_name = tree.decode(encoded_name)
    print(decoded_name)
    print("Довжина закодованої послідовності:", len(decoded_name))

    print()
    print("Нерівність Крафта")
    if tree.check_kraft_inequality():
        print("Нерівність виконується")
    else:
        print("Нерівність не виконується")

    print()
    print("Ентропія вихідного повідомлення:", tree.calculate_entropy_of_dist())
    print("Очікувана довжина вихідного повідомлення:", tree.calculate_expected_len())


def make_lab_for_dist(dist):
    tree = HuffmanTree()
    tree.build_freq_table_distribution(dist)
    tree.build_p_table()
    tree.build_tree()
    tree.build_codes()

    print("Кодові слова:", tree.codes)
    print("Довжини кодових слів:", tree.code_lens)
    tree.draw_tree()

    print()
    print("Нерівність Крафта")
    if tree.check_kraft_inequality():
        print("Нерівність виконується")
    else:
        print("Нерівність не виконується")

    print()
    print("Ентропія розподілу:", tree.calculate_entropy_of_dist())
    print("Очікувана довжина послідовності:", tree.calculate_expected_len())


if __name__ == '__main__':
    name: str = "Майор Роман Юрійович"
    dist = [0.11, 0.08, 0.13, 0.06, 0.06, 0.11, 0.11, 0.09, 0.11, 0.13]

    make_lab_for_str(name)
    print()
    print()
    make_lab_for_dist(dist)

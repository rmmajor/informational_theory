import math

# Завдання 1
print('Завдання 1')

# Створення таблиці ймовірностей p(xi,yk) згідно з вказаними значеннями в таблиці 1.
probabilities = [
    [0.075, 0.020, 0.100],
    [0.020, 0.300, 0.025],
    [0.005, 0.080, 0.375]
]

# Розрахунок ентропії виходу каналу H(Y).
hy = 0
for k in range(len(probabilities[0])):
    pk = sum(probabilities[i][k] for i in range(len(probabilities)))
    hy += -pk * math.log2(pk) if pk > 0 else 0

print(f"H(Y) = {hy:.3f} біт")

# Розрахунок умовної ентропії виходу каналу при відомому вході H(Y|X).
hyx = 0
for i in range(len(probabilities)):
    px = sum(probabilities[i])
    for k in range(len(probabilities[i])):
        if probabilities[i][k] > 0:
            hyx += -probabilities[i][k] * math.log2(probabilities[i][k] / px)

hyx /= len(probabilities)
print(f"H(Y|X) = {hyx:.3f} біт/символ")

# Розрахунок середньої кількості інформації, що переноситься одним символом.
ixy = hy - hyx
print(f"I(Y,X) = {ixy:.3f} біт/символ")

c = 0
for i in range(len(probabilities)):
    px = sum(probabilities[i])
    hyx = 0
    for k in range(len(probabilities[i])):
        if probabilities[i][k] > 0:
            hyx += -probabilities[i][k] * math.log2(probabilities[i][k] / px)
    ixy = hy - hyx
    c = max(c, ixy)

print(f"C = {c:.3f} біт/символ")

# Завдання 2
print()
print('Завдання 2')

# Вхідні дані, ймовірності правильного прийому, помилки та витирання
q = 0.95
pP = 0.01
pV = 0.04

# Обчислення пропускної здатності
Hp = - (pP * math.log2(pP) + (1 - pP) * math.log2(1 - pP))
C = 1 - Hp

# Виведення результату
print(f"C = {C:.3f} біт/символ")
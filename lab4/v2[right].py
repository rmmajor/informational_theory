import math

# Завдання 1
print('Завдання 1')

# Створення таблиці ймовірностей p(xi,yk) згідно з вказаними значеннями в таблиці 1.
probabilities = [
    [0.170, 0.035, 0.010],
    [0.020, 0.595, 0.005],
    [0.010, 0.070, 0.085],
]

# Розрахунок ентропії виходу каналу H(Y).
hy = 0
for k in range(len(probabilities[0])):
    pk = sum(probabilities[k])
    hy += -pk * math.log2(pk) if pk > 0 else 0
    print(f"p{k+1:.0f}: {pk:.3f}  log: {math.log2(pk)}")

print(f"H(Y) = {hy:.3f} біт")

# Розрахунок умовної ентропії виходу каналу при відомому вході H(Y|X).
hyx = 0
px1 = 0
px = 0
for i in range(len(probabilities)):
    for k in range(len(probabilities[i])):
        px = sum(probabilities[i][k] for i in range(len(probabilities)))
        # print([str(probabilities[i][k]) + ' + ' for i in range(len(probabilities))], end=" = ")
        # print(px)
        if probabilities[i][k] > 0:
            hyx += -probabilities[i][k] * math.log2(probabilities[i][k] / px)
            print(f'{probabilities[i][k]} * log2({probabilities[i][k]} / {px})')
    px1 += px

#print(px1)

print(f"H(Y|X) = {hyx:.3f} біт")
print(px1)

# Розрахунок середньої кількості інформації, що переноситься одним символом.
ixy = hy - hyx
print(f"I(Y,X) = {ixy:.3f} біт")

c = math.log2(3) - hyx
print(f"C = {c:.3f} біт")

# Завдання 2
print('Завдання 2')

# Вхідні дані, ймовірності правильного прийому, помилки та витирання
q = 0.94
pP = 0.01
pV = 0.05

C = q * math.log2(q) + pP * math.log2(pP) - (q + pP) * math.log2((q + pP) / 2)
hy = - (q + pP) * math.log2((q + pP) / 2) - pV * math.log2(pV)
hyx = - q * math.log2(q) + pP * math.log2(pP) - pV * math.log2(pV)

# Виведення результату
print(f"C = {C:.3f} біт")
print("hy", hy)
print("hyx", hyx)

import random
import math

n = random.randint(10, 20)
print(n)


px = {}
array = []
_sum = 0
for i in range(n):
    elem = random.randint(0, 10)
    array.append(elem)
    if elem in px:
        px[elem] += 1
    else:
        px[elem] = 1

myKeys = list(px.keys())
myKeys.sort()
sorted_px = {i: px[i] for i in myKeys}

for k, v in sorted_px.items():
    p = v/n
    print(f"p({k}) = {v}/{n} = {round(p, 2)}")

for k, v in sorted_px.items():
    p = v/n
    _sum += -p * math.log(p, 2)
    print(f"{round(p, 2)} * {-1 * round(math.log(p, 2), 2)} + ", end='')

print()
print("Кількість елементів:", n)

print("Ентропія:", _sum)

print("Массив: ", array)

print("Кількість повторень:", sorted_px)

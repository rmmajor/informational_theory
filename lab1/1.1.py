import random
import math

dist = [0.11, 0.08, 0.13, 0.06, 0.06, 0.11, 0.11, 0.09, 0.11, 0.13]
ans = 0

for x in dist:
    ans += x * math.log2(x)
    print(f"{x} * {round(math.log2(x), 2) * -1} + ", end='')

print()
print(ans)

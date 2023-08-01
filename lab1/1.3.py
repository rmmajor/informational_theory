from PIL import Image
import numpy as np
from math import log2
import matplotlib.pyplot as plt

file_name = 'image.png'
img = Image.open(file_name).convert("L")

data = np.array(img.getdata(), dtype=np.uint8)
plot = [0 for x in range(256)]


for x in data:
    plot[x] += 1

plt.plot([x for x in range(1, 257)], plot)

eumivinist = [float(x) / len(data) for x in plot]

entropy = -sum([x * log2(x) for x in eumivinist if x > 0])
print(round(entropy, 3))

plt.show()

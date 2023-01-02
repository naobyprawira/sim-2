
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

## Random Walk untuk pergerakan sebuah partikel di bidang 2D

N = 100
movement = [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]]
x = [[0, 0]]  # lintasan posisi partikel
xs = [0, 0]  # posisi awal partikel
for i in range(N):
    rd = random.choices(movement, [1, 1, 1, 1, 1], k=1)[0]
    x.append([xs[0]+rd[0], xs[1]+rd[1]])
    xs[0] = xs[0]+rd[0]
    xs[1] = xs[1]+rd[1]

# Visualisasi
x = np.array(x)
xmin = np.min(np.array(x)[:, 0])
xmax = np.max(np.array(x)[:, 0])
ymin = np.min(np.array(x)[:, 1])
ymax = np.max(np.array(x)[:, 1])
for i in range(1, N+1):
    fig, ax = plt.subplots(1, figsize=(5, 5))
    ax.set_xlim(xmin-1, xmax+1)
    ax.set_ylim(ymin-1, ymax+1)
    ax.plot(x[:i, 0], x[:i, 1])
    plt.show()
import numpy as np


def sample():
    x = 0
    for _ in range(2):
        x += np.random.choice([1, 2, 3, 4, 5, 6])
    return x


trial = 100
V, n = 0, 0
for _ in range(trial):
    s = sample()
    n += 1
    V += (s - V) / n
    print(V)

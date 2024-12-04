import math
import matplotlib.pyplot as plt
from random import random
import numpy as np

class Point:
    point = []
    def __init__(self, x, y):
        self.point = [x, y]
    def evolution(self):
        a = math.fmod(2 * self.point[0] + self.point[1], 1)
        b = math.fmod(self.point[0] + self.point[1], 1)
        self.point[0] = a
        self.point[1] = b
    def inv_evolution(self):
        a = math.fmod(self.point[0] - self.point[1], 1)
        b = math.fmod((-self.point[0]) + 2.0 * self.point[1], 1)
        self.point[0] = a
        self.point[1] = b

init_points = []
evol_points = []

for i in range(0, 1000):
    p = Point(np.random.uniform(0.4, 0.6), np.random.uniform(0.4, 0.6))
    init_points.append(p)

for i in init_points:
    plt.plot(i.point[0], i.point[1], markersize = 0.7, marker='o', color = 'black')

for i in init_points:
    for j in range (0, 100):
        i.evolution()
        if j == 99:
            evol_points.append(i)
    plt.plot(i.point[0], i.point[1], markersize = 0.5, marker='o', color = 'red')

for i in evol_points:
    for j in range (0, 100):
        i.inv_evolution()
    if i.point[0] < 0:
        i.point[0] = -i.point[0]
    if i.point[1] < 0:
        i.point[1] = -i.point[1]
    plt.plot(i.point[0], i.point[1], markersize = 0.5, marker = 'o', color = 'blue')

plt.show()
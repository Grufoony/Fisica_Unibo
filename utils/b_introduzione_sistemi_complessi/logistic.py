from hashlib import new
from random import randint, random
import matplotlib.pyplot as plt

class Person:
    point = []
    Dim = 100
    life_points = 10000
    def __init__(self, x, y):
        self.point = [x, y]
    def evolution(self, randx, randy):
        self.life_points = self.life_points - 1
        self.point[0] = self.point[0] + randx
        self.point[1] = self.point[1] + randy
        if self.point[0] >= self.Dim or self.point[1] >= self.Dim:
            self.point[0] = randint(-self.Dim, self.Dim)
            self.point[1] = randint(-self.Dim, self.Dim)
        elif self.point[0] <= -self.Dim or self.point[1] <= -self.Dim:
            self.point[0] = randint(-self.Dim, self.Dim)
            self.point[1] = randint(-self.Dim, self.Dim)
    def neigh(self):
        a11 = [self.point[0] - 1, self.point[1] + 1]
        a12 = [self.point[0], self.point[1] + 1]
        a13 = [self.point[0] + 1, self.point[1] + 1]
        a21 = [self.point[0] - 1, self.point[1]]
        a22 = [self.point[0], self.point[1]]
        a23 = [self.point[0] + 1, self.point[1]]
        a31 = [self.point[0] - 1, self.point[1] - 1]
        a32 = [self.point[0], self.point[1] - 1]
        a33 = [self.point[0] + 1, self.point[1] - 1]
        neigh_table = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
        return neigh_table

class Population:
    persons = []
    def add_person(self, person):
        self.persons.append(person)
    def num(self):
        return len(self.persons)
    def plot_population(self):
        for i in self.persons:
            plt.plot(i.point[0], i.point[1], marker='o', color = 'green')
    def evolution(self):
        for i in self.persons:
            i.evolution(randint(-2, 2), randint(-2, 2))
    def population_increment(self):
        r = randint(0, 100)
        if r <= 100:
            person = Person(randint(-100, 100), randint(-100, 100))
            self.persons.append(person)
    def population_control(self):
        for i in self.persons:
            if i.life_points == 0:
                self.persons.remove(i)
    def neigh_control(self):
        for i in range (0, len(self.persons)):
            for j in range (i + 1, len(self.persons)):
                for k in range (0, 9):
                    if self.persons[i].neigh()[k] == self.persons[j].neigh()[k]:
                        self.persons[j].life_points = 0

plt.ion()
# Create Persons
population = Population()
for i in range (0, 1):
    person = Person(randint(-100, 100), randint(-100, 100))
    population.add_person(person)

X = []
Y = []

for j in range (0, 2000):
    plt.subplot(1, 2, 1)
    plt.plot(-100, -100)
    plt.plot(100, -100)
    plt.plot(-100, 100)
    plt.plot(100, 100)
    population.evolution()
    population.plot_population()
    population.neigh_control()
    population.population_increment()
    population.population_control()
    plt.subplot(1, 2, 2)
    X.append(j)
    Y.append(population.num())
    plt.plot(X, Y, markersize=0.7, marker='o', color = 'blue')
    plt.grid()
    plt.pause(0.001)
    plt.draw()
    plt.clf()
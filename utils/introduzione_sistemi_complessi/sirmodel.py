from hashlib import new
from random import randint, random
import matplotlib.pyplot as plt

class Person:
    poss_states = ['S', 'I', 'R']
    state = poss_states[0]
    point = []
    Dim = 20
    T_infect = 10
    def __init__(self, x, y):
        self.point = [x, y]
    def infect(self):
        self.state = self.poss_states[1]
    def evolution(self, randx, randy):
        if self.state == 'I':
            if self.T_infect > 0:
                self.T_infect = self.T_infect - 1
            elif self.T_infect == 0:
                self.state = self.poss_states[2]
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
    def count_state(self):
        c_s = 0
        c_i = 0
        c_r = 0
        for i in range (0, len(self.persons)):
            if self.persons[i].state == 'I':
                c_i = c_i + 1
            elif self.persons[i].state == 'S':
                c_s = c_s + 1
            elif self.persons[i].state == 'R':
                c_r = c_r + 1
        a = [c_s, c_i, c_r]
        return a
    def plot_population(self):
        for i in self.persons:
            if i.state == 'S':
                plt.plot(i.point[0], i.point[1], markersize = 5.5, marker = 'o', color = 'green')
            elif i.state == 'I':
                plt.plot(i.point[0], i.point[1], markersize = 5.5, marker = 'o', color = 'red')
            elif i.state == 'R':
                plt.plot(i.point[0], i.point[1], markersize = 5.5, marker = 'o', color = 'blue')
    def evolution(self):
        for i in self.persons:
            i.evolution(randint(-2, 2), randint(-2, 2))
    def neigh_control(self):
        for i in range (0, len(self.persons)):
            if self.persons[i].state == 'I':
                for j in range (0, len(self.persons)):
                    for k in range (0, 9):
                        if self.persons[i].neigh()[k] == self.persons[j].neigh()[k]:
                            self.persons[j].infect()

plt.ion()
# Create Persons
population = Population()
for i in range (0, 600):
    person = Person(randint(-20, 20), randint(-20, 20))
    population.add_person(person)

population.persons[0].infect()
population.persons[1].infect()
population.persons[2].infect()
population.persons[3].infect()

X = []
Y1 = []
Y2 = []
Y3 = []

for j in range (0, 100):
    plt.subplot(1, 2, 1)
    plt.plot(-20, -20)
    plt.plot(20, -20)
    plt.plot(-20, 20)
    plt.plot(20, 20)
    population.evolution()
    population.plot_population()
    population.neigh_control()
    a = population.count_state()
    plt.subplot(1, 2, 2)
    X.append(j)
    Y1.append(a[0])
    Y2.append(a[1])
    Y3.append(a[2])
    plt.plot(X, Y1, markersize=0.7, marker = 'o', color = 'green')
    plt.plot(X, Y2, markersize=0.7, marker = 'o', color = 'red')
    plt.plot(X, Y3, markersize=0.7, marker = 'o', color = 'blue')
    plt.plot()
    plt.grid()
    plt.pause(0.001)
    plt.draw()
    plt.clf()
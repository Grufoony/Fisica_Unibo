from random import randint, random
import matplotlib.pyplot as plt

class Micro:
    n = 1
    def upgrade(self):
        self.n = self.n + 1
    def downgrade(self):
        self.n = self.n - 1

class Macro:
    square = []
    def add(self, element):
        self.square.append(element)
    def size(self):
        return len(self.square)
    def evolve(self):
        i = randint(0, 399)
        j = randint(0, 399)
        if self.square[j].n != 0:
            self.square[i].upgrade()
            self.square[j].downgrade()

macro = Macro()
for i in range(0, 400):
    micro = Micro()
    macro.add(micro)

for j in range (0, 100000):
    macro.evolve()

plt.ion()
a = []
bins_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for o in macro.square:
    a.append(o.n)
    plt.hist(a, bins = bins_list)
    #plt.xlim(0, 14)
    #plt.ylim(0, 5100)
    plt.show()
    plt.grid()
    plt.pause(0.001)
    plt.draw()
    plt.clf()

#for k in range(0, 100):
#    for h in range(0, 100):
#        print(macro.square[10 * k + h].n, end=' ')
#    print('')
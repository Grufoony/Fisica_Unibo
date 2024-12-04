# Made by Grufoony

import random as rnd
import time 
import os
import numpy as np
import matplotlib.pyplot as plt
import boltzmann as b
 
class board:
	def __init__(self,nrows=5,ncols=5,pocket=5):
		self.nrows = nrows
		self.ncols = ncols
		self.nodes = [pocket for i in range(nrows*ncols)]
	def print(self):
		i = 0
		for element in self.nodes:
			print(element, end=' ')
			i += 1
			if i == self.ncols:
				print('\n')
				i = 0
	def neighbors(self,pos):
		neighbors = []
		if pos % self.ncols == 0: 
			neighbors.append(pos + 1)
		elif (pos+1) % self.ncols == 0:
			neighbors.append(pos - 1)
		else:
			neighbors.append(pos + 1)
			neighbors.append(pos - 1)
		if pos < self.ncols:
			neighbors.append(pos + self.ncols)
		elif (pos >= self.ncols*(self.nrows - 1)) and (pos < self.ncols*self.nrows):
			neighbors.append(pos - self.ncols)
		else:
			neighbors.append(pos + self.ncols)
			neighbors.append(pos - self.ncols)
		return neighbors
	def evolve(self):
		for pos in range(len(self.nodes)):
			neighbour = rnd.choice(self.neighbors(pos))
			if rnd.uniform(0,1) < 0.5:
				self.nodes[pos] += 1
				if self.nodes[neighbour] > 0:
					self.nodes[neighbour] -= 1
			else:
				if self.nodes[pos] > 0:
					self.nodes[pos] -= 1
				self.nodes[neighbour] += 1
	def data(self):
		x = np.arange(0, max(self.nodes)+1)
		y = np.zeros(max(self.nodes)+1)
		for element in self.nodes:
			y[element] += 1
		return x,y
		
myboard = board(50, 50)	

for i in range(99):
	start = time.time_ns()
	myboard.evolve()	
	finish = time.time_ns()
	print("el",(finish-start)/1000000000)
data = myboard.data()
plt.plot(data[0],data[1])
plt.show()

cdata = b.simulate(100,100,5) 
plt.plot(cdata[0],cdata[1])
plt.show()

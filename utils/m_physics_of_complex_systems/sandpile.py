# Made by SimonB00

import random as rnd
import time 
import os
 
class graph:
	def __init__(self,nrows=5,ncols=5):
		self.nrows = nrows
		self.ncols = ncols
		self.nodes = [0 for i in range(nrows*ncols)]
	def printgraph(self):
		olink = '---'
		vlink = '|'
		space = '   '

		for j in range(self.nrows):
			bottom = ''
			for i in range(self.ncols):
				if i == self.ncols-1:
					print(str(self.nodes[i + self.ncols*j]))
					bottom += vlink
					break
				print(str(self.nodes[i + self.ncols*j]) + olink,end='')
				bottom += vlink + space
			if j != self.nrows-1:
				print(bottom)
	def neighbors(self,pos):
		neighbors = []
		if pos in range(0,self.ncols*self.nrows,self.ncols):
			neighbors.append([pos + 1])
		elif pos in range(self.ncols-1,self.ncols*self.nrows,self.ncols):
			neighbors.append([pos - 1])
		else:
			neighbors.append([pos + 1])
			neighbors.append([pos - 1])
		if pos in range(self.ncols):
			neighbors.append([pos + self.ncols])
		elif pos in range(self.ncols*(self.nrows-1),self.ncols*self.nrows):
			neighbors.append([pos - self.ncols])
		else:
			neighbors.append([pos + self.ncols])
			neighbors.append([pos - self.ncols])
		return neighbors
	def redistribute(self,pos):
		self.nodes[pos] = 0
		if pos in range(0,self.ncols*self.nrows,self.ncols):
			self.nodes[pos + 1] += 1
		elif pos in range(self.ncols-1,self.ncols*self.nrows,self.ncols):
			self.nodes[pos - 1] += 1
		else:
			self.nodes[pos + 1] += 1
			self.nodes[pos - 1] += 1
		if pos in range(self.ncols):
			self.nodes[pos + self.ncols] += 1
		elif pos in range(self.ncols*(self.nrows-1),self.ncols*self.nrows):
			self.nodes[pos - self.ncols] += 1
		else:
			self.nodes[pos + self.ncols] += 1
			self.nodes[pos - self.ncols] += 1
	def check(self):
		for pos in range(len(self.nodes)):
			if self.nodes[pos] >= 4:
				self.redistribute(pos)
				pos = 0

mygraph = graph(10,10)				
mygraph.printgraph()

while True:
	os.system('clear')
	pos = int(mygraph.nrows*mygraph.ncols*rnd.random())
	mygraph.nodes[pos] += 1
	
	if mygraph.nodes[pos] == 4:
		mygraph.redistribute(pos)
	mygraph.check()
	mygraph.printgraph()
	time.sleep(0.5)

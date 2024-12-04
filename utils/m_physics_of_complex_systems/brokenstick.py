import random
import matplotlib.pyplot as plt

class stick:
	def __init__(self):
		self.stick = [1]
		self.ncuts = 1
	def breakstick(self):
		len_ = self.stick[-1]
		cut = random.uniform(0,len_)
		self.stick.append(cut)
		self.ncuts += 1
	def plot(self):
		plt.plot(range(self.ncuts),self.stick)	
		plt.yscale('log')
		plt.show()

mystick = stick()
for i in range(500):
	mystick.breakstick()
mystick.plot()

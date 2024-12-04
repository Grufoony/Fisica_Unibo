import random as rd
numbers = []
leng = []
rd1 = rd.random()
numbers.append(rd1)
leng.append(rd1)
for i in range(0, 100):
    rd2 = rd.random()
    if rd2 > rd1:
        numbers.append(rd2)
        rd1 = rd2
for i in range (0, len(numbers) - 1):
    leng.append(numbers[i + 1] - numbers[i])
import random

def dice():
	while True:
		n = random.randint(1,6)
		yield n

for number in dice():
	print(number)

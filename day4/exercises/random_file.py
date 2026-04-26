from random import *

very_random = randint(1, 50)
print(very_random)

very_random = round(uniform(1, 50), 2)
print(very_random)

very_random = random()
print(very_random)

colours = ["Blue", "Green", "Yellow", "Red", "Purple"]
very_random = choice(colours)
print(very_random)

numbers = list(range(5, 50, 5))
shuffle(numbers)
print(numbers)
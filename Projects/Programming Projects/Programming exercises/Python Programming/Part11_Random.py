import random

#print(help(random))

# random integers
low = 1
high = 100
number = random.randint(low,high)
print(number)

# random choices for strings
options = ("rock", "paper", "scissor")
option = random.choice(options)
print(option)

# shuffle for list
cards = ["1", "2", "3", "4", "5"]
random.shuffle(cards)
print(cards)

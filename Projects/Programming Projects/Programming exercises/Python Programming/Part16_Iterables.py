# Iterables = An object/collection that can return its  elements one at a s time
#               allowing it to be iterated over in a loop

#example 1
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
print("-----------------------")
#example 2
for number in reversed(numbers):
    print(number)
print("-----------------------")
#example 3
for number in numbers:
    print(number, end=" ")
print()
print("-----------------------")
#example 4
name = "Angelo"
for n in name:
    print(n, end=" ")
print()
# All of this can be applied also in tuples, sets
# but sets CANT BE REVERSED

# Dictionary examples

alphabet = {"A": 1, "B": 2, "C": 3}

for value in alphabet.values(): #values only
    print(value)

for key in alphabet.keys(): #keys only
    print(key)

for a, b in alphabet.items(): #keys and values
    print(a, b)

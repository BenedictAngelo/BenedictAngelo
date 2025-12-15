# collection = single "variable" used to store multiple values
# List [] = ordered and changeable. Duplicates
# Set {} unordered and immutable, but Add/Remove OK. No Duplicates
# Tuple () ordered and unchangeable. Duplicates and is FASTER

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

for fruit in fruits:
    print(fruit)

print("apple" in fruits)

# append means add
fruits.append("pineapple")
print(fruits)

# remove means remove something on List
fruits.remove("apple")
print(fruits)

# insert add but specify which position
fruits.insert(0, "kiwi")
print(fruits)

# sort means to arrange in alphabetical ordered
fruits.sort()
print(fruits)

# reverse means to reverse position on typed List
fruits.reverse()
print(fruits)

# clear means to remove all
# index for locate the position of string
print(fruits.index("pineapple"))

# counts means to count how many of the same input
fruits.append("pineapple")
print(fruits.count("pineapple"))

# sets {} = unordered immutable and changes order each run
vegetables = {"broccoli, spinach, carrot, potato"}
print(vegetables)

# add is to add something in sets
vegetables.add("tomato")
print(vegetables)

# remove also applies

# pop - removes the first item but sets is random
vegetables.pop()
print(vegetables)
# clear also applies

# tuples can only have count and index

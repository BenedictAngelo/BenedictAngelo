# list comprehension =  A concise to create lists in Python
#                    compact and easier to read than traditional loops
#                    [expression for value in iterable if condition]

double = []
for x in range(1,11):
    double.append(x*2)
print(double)

# improved
doubles = [x * 2 for x in range(1,11)]
print(doubles)

triples = [y * 3 for y in range(1,11)]
print(triples)

fruits = ["apple","orange","banana","coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars())

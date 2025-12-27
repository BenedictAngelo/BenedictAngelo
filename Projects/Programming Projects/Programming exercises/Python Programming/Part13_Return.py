# return = statement used to end a function
#           and send a result back to the caller

def add(x, y):
    z = x + y
    return z
def subtract(x, y):
    z = x - y
    return z

print(add(30,12))
print(subtract(40,33))

def create_name (first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("benedict","angelo")
print(full_name)

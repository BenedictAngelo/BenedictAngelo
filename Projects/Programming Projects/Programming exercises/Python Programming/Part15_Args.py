# *args = allows you to pass multiple non-key arguements
# **kwargs =  allows you to pass multiple keyword-arguments
#           * unpacking operator
#           1 positional 2 default 3 keyword 4 ARBITRARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4))

# another example
def display_name(*names):
    for name in names:
        print(name, end=" ") #its tuple

display_name("Benedict", "Angelo", "A.", "Bumatay")

# another example
def print_address(**kwargs): 
    print(kwargs)

print_address(street="123 street",  # it became a dictionary
              city="1234 City",
              zip="4567")



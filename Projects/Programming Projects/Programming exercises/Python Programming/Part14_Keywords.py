# keywords arguments =  an arguments preceded by an identifier
#                       helps with readability
#                       orders of arguments does not matter
#                       1 positional 2 default 3 keyword 4 arbitrary
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Benedict", "Bumatay")
# applying keywords
hello("Hello", title="Mr.", last="Benedict", first="Bumatay")

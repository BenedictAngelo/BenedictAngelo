# if __name__ = __main__: this script can be imported OR run standalone
# Fucntions and classes in this can be reused without the main block of code executing
# Good practice ( code is modular
#               helps readability
#               leaves no global variables
#               avoid unintended execution)
#
#               Ex. library = import library for functionality
#                               when running library directly, display a help page




from script2 import * # '*' import everything

# prints __main__
print(__name__) # prints the name of the file if imported

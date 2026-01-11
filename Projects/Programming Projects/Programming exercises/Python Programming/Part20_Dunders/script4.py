# it wont execute the main() of script3

from script3 import *


def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

print("This is script4")
favorite_food("fries") # came from script3
favorite_drink("shake")
print("Goodbye")


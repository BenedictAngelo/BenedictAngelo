# While loop = execute some cods WHILE some conditions are true

age = (input("What is your age? (q to quit) "))

if age.lower() == "q" :
    exit()
else:
    pass

while age == "" or age.isdigit() == False:
    print("Invalid input")
    age = str(input("What is your age? "))
print(f"you are {age} years old")

food = input("What is your favorite food? (q to quit) ")

while not food == "q" and food.isdigit() == False:
    print(f"Your favorite food is {food}")
    break
else:
    print("Invalid input")
    food = input("What is your favorite food? (q to quit) ")


exit()
    





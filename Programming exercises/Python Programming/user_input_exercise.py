# Validate user input
# 1. Must not be more than 20 characters
# 2. Must not contain digits
# 3. if contains space, must announce

name = input("What is your name? ")
name_digitcheck = name.isalpha()
name_spacecheck = name.find(" ")
name_dotcheck = name.find(".")

if name_digitcheck == True:
    print(name)
elif name_digitcheck == False and not name_spacecheck == -1 or not name_dotcheck == -1 and len(name) > 20 :
    print(name)
    print(f"your name contains space in the '{name_spacecheck}' character postion" 
    if not name_spacecheck == -1 else print())
    print(f"your name contains dot in the '{name_dotcheck}' character postion" 
    if not name_dotcheck == -1 else print())
else:
    print("Invalid Input, name must not contain digits and above 20 characters")



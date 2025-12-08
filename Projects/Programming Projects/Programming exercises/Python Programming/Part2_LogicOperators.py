#Logical operators

Age = int(input("What is your age? "))
Employed = input("Are you employed? (Y/N)")

if Age > 18 or Age == 18:                                   # 'or' at least one condition is true
    print("You're an adult")
else:
    print("You're underage")


# using both 'and' and 'or' operators

if Age >= 18 and (Employed == "Y" or Employed == "y"):       # 'and' both conditions must be true     
    print("and you are a provider")
elif Age < 18 and (Employed == "Y" or Employed == "y"):
    print("and you are a child laborer")
elif Age >= 18 and Age < 60 and (Employed == "N" or Employed== "n"):
    print("and you need a job")
elif Age < 18 and (Employed == "N" or Employed == "n"):
    print("and you must go to school")
else:
    pass

# using 'not' operator

yes_employed = bool(Employed == "Y" or Employed == "y")

if Age >= 60 and not yes_employed:                            # 'not' flips the condition for the boolean variable
    print("and is already retired")
elif Age > 18 and Age <60 and yes_employed:
    print("and keep working")

    # conditional expression
print("but you must RIP" if Age >= 100 else print())   # basically a one line shortcut



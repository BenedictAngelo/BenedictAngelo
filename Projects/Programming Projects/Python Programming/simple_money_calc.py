base_money = input("How much money do you have right now? ")
operator = input("What do you want to do with it? (-,+,/,*) ")
amount = input("To what amount? ")
print()

if base_money == "":
    print("Invalid input")
elif amount == "":
    print("Invalid input")
elif operator == "+":
    total = float(base_money) + float(amount)
    print(f"You now have {str(total)} AED")
elif operator == "-":
    total = float(base_money) - float(amount)
    print(f"You now have {str(total)} AED")
elif operator == "/":
    total = float(base_money) / float(amount)
    print(f"You now have {str(total)} AED")
elif operator == "*":
    total = float(base_money) * float(amount)
    print(f"You now have {str(total)} AED")
else:
    print(f"{operator} operator is invalid")


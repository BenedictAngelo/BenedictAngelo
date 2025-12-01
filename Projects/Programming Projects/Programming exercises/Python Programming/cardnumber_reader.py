# creating a card number reader
# 1, Must increment in 4 characters and 4 groups
# 2. Must only contain digits
# 3. Must repeat the last 4 digits
print("Enter your card number: ")

cardnumber = (f"{input()}-{input()}-{input()}-{input()}")
digitcheck1 = cardnumber[1:3].isdigit()
digitcheck2 = cardnumber[5:8].isdigit()
digitcheck3 = cardnumber[10:13].isdigit()
digitcheck4 = cardnumber[15:18].isdigit()


if cardnumber[4] != "-" or cardnumber[9] != "-" or cardnumber[14] != "-":
    print("Invalid card number, make sure to type 4 character in each input")
elif digitcheck1 == False or digitcheck2 == False or digitcheck3 == False or digitcheck4 == False:
    print("Invalid card number, make sure to type only digits")
elif len(cardnumber) >=20:
    print("Invalid input, must not exceed 20 characters")
else:
    print(f"Does your number ends in?: XXXX-XXXX-XXXX-{cardnumber[-4:]}")





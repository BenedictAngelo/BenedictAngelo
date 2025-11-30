# len() counts the number of characters, only works on string
Name = input("What is your name? ")
print(len(Name))

# .find() finds the position of the input, finds the first if there is multiple
# , .rfind() is for last
print([Name.find("e"), Name.rfind("e")])

# .capitalize() first letter of string is upper case
Name = Name.capitalize()
print(Name)
# .upper() makes it all upper case and .low() all lower case
Name = Name.upper()
print(Name)
Name = Name.lower()
print(Name)

# .isalpha() will check if the input all contains alphabet characters
# , will retun false if its not
# isdigit() for numbers
Name = Name.isalpha()
print(Name)

number = input("What is your phone number? ")
is_all_digits = number.isdigit()
print(is_all_digits)

# .replace("old", "new") will replace the character to new one
if not is_all_digits:
    # For example, let's remove dashes and spaces
    cleaned_number = number.replace("-", "").replace(" ", "")
    print(f"Cleaned number: {cleaned_number}")

# for more string helper type print(help(str))
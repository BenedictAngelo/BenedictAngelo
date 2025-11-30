## Strings
First_Name = "Benedict Angelo"
Surname = "Bumatay"
Middle_Name = "Aguirre"
Birth_month = "July"

print(f"Hi my name is, {First_Name} {Middle_Name} {Surname}")

##Integers
Age = 24
Birthday = 23
Birth_year = 2001

print(f"My birthday is, {Birth_month} {Birthday} {Birth_year}")

##Boolean
Is_student = False
Employement = False

if Is_student == True:
    print("Yes, I am a student")
else:
    print("No, I am not a student anymore")

if Employement == True:
    print("I am employed")
else:
    print("I am unemployed")

##float

Money_amount = 50.00
Country_bill = "AED"
Money = (str(Money_amount) + " AED") #used str() to convert a float into string
print(f"The amount of my money right now is: {Money}")

##variable convert
##str()
##bool()
##int()
##float()

##To know what type: type()
##sample:

#print(type(Money_amount))
#print(bool(First_Name)) #will become false if te variable is empty

#To use user input: input()

#Full_Name = input("What is my name? ")
#print(f"My full name is, {Full_Name}.")

#Typed_Age = input("What is my Age? ")
#print(f"I am {Typed_Age} years old")

#if int(Typed_Age) >= 18:
#    print("Yes I am an adult")
#else:
#    print("I am underage")

#simple arithmetic
Money_to_add = input("How much will I add to my money? ")
Money_want = float(Money_amount) + float(Money_to_add)
print(f"Total of my desired money is: {Money_want} AED")





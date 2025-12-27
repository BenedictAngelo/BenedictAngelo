import random
# must be 24 characters
# must contain special characters
# must contain capital letters
# must contain lower case letters
# must contain digits
uppercase = ["A","B","C","D"]
lowercase = list(s.lower() for s in uppercase)
special = ["@","#","!","-"]
group = uppercase,lowercase,special
characters_number = 24
password = ""
while password == "" :
    for x in group.range(characters_number):
        generator = random.choice(x)
        print(generator)
    break
    

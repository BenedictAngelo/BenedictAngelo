# indexing - accessing elements of a sequence [ ] (indexing operator)
# [start:end:stop]
Name = "Benedict Angelo A. Bumatay"

print(Name[0]) # start only

print(Name[0:8]) # start and end
        #or
print(Name[:8])

print(Name[8:])

print(Name[-1]) # starts at the last character

print(Name[::2]) # prints every 2 chracter of the string

print(Name[::-1]) # Basically reverse the whole string

# simple exercise

card_number = "1234-5678-9123-4567"
print(f"XXXX-XXXX-XXXX-{card_number[-4:]}")


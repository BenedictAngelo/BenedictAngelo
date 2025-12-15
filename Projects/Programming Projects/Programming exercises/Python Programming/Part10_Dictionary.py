# dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates

bio = {"First Name": "Benedict Angelo",
       "Middle Name": "Aguirre",
       "Last Name": "Bumatay",
       "Birthday": "July 23 2001",
       "Age": "24"}
# to get values:
print(bio.get("First Name"))

# if nothing
print(bio.get("Name"))

# dictionary check
if bio.get("First Name"):
    print("There is no input")
else:
    print("Not typed yet")

# to add or replace in dictionary:
bio.update({"Full Name": "Benedict Angelo A. Bumatay"})
# bio.update({"First Name": "Benedict Angelo A. Bumatay"})
print(bio)

# to remove in dictionary
bio.pop("First Name") #remove curly braces
# to remove latest
# bio.popitem()
print(bio)

# to delete all 
# bio.clear()

# to get keys only
keys = bio.keys()
print(keys)
# to get values only
values = bio.values()
print(values)

# iterate
for key in keys:
    print(key)
for value in values:
    print(value)

# items for listing
items = bio.items()
print(items)

#iterate
for key,value in items:
    print(f"{key}: {value}")





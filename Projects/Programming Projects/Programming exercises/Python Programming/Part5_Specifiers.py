# format specifies: {value:flags} format a value based
#  on what flags are inserted

print("How much is that phone?")

price1 = 300.545454

print(f"So that phone is {price1}$ ?")
# make it so that it only prints on 2 decimal point
print(f"Why does it have that {price1:.2f}$ cents?")

print(f"price:{price1:10}")
print()

price2 = 200.1234
price3 = 400.3456786786
# left align
print(f"price:{price1:>10}$")
print(f"price:{price2:>10}$")
print(f"price:{price3:>10}$")
print()
# right align
print(f"price:{price1:<10}$")
print(f"price:{price2:<10}$")
print(f"price:{price3:<10}$")
print()
# middle align
print(f"price:{price1:^10}$")
print(f"price:{price2:^10}$")
print(f"price:{price3:^10}$")
print()

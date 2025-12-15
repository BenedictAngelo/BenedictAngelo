fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "beef"]

groceries = [fruits, vegetables, meats]

print(groceries)
# indexing
print(groceries[0])
print(groceries[0][0])

# to iterate
for cart in groceries:
    # print(cart)
    # to iterate whats inside
    for single in cart:
        print(single)
# grid like
for cart in groceries:
    # print(cart)
    # to iterate whats inside
    for single in cart:
        print(single, end=" ")
    print()

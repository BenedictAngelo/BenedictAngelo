# for loops = execute a block of code a fixed number of times
# can iterate over a range , string, sequence, etc.abs

for i in range(1, 11):
    print(i)
# reverse
for x in reversed(range(1, 11)):
    print(x)

print("Time is up")

for n in range(1, 21):
    if n == 13:
        break
    else:
        print(n)

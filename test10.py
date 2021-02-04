# lists in python
# new items placed at the end of the list
# order is maintained and duplicates are allowed

animals = ['Bird','Cat','Dog','Elephant','Fish']
print(animals[:])
print(animals[:-2])
print(animals[-2:])

myNums = [10,22,45,4,-6,44,25]
print(myNums[:])
max = myNums[0]
for item in myNums:
    if item > max:
        max = item
print(f"largest is {max}")
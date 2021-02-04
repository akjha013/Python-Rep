# dictionary example in python
digs ={
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}
phone = input('Phone: ')
output = ""
for dig in phone:
    # output+= digs.get(dig,"!") + " "
    output+= digs[dig]+" "
print(output)




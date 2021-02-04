# dictionaries for emoji converter
msg = input('>')
# split words into a list
words = msg.split(' ')
emoji = {
    ":)" : "😊",
    ":(" : "😢"
}
# print(words)
output = ""
for word in words:
    output += emoji.get(word,word) + " "
print(output)
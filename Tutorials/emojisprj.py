message = input('<')
words = message.split(' ')
Emojis = {
    ":)": "😀",
    ":(": "😞"
}
output = " "
for word in words:
    output += Emojis.get(word, word)
print(output)

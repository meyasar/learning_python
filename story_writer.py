words = ""
while True:
    word = input("Please type in a word:")
    if word == "end":
        break
    if len(words) and words.split()[-1] == word:  
        break  
    words += word + " "
print(words)
def search(text,word):
    if word in text:
        return "Word found"
    else:
        return "Word not found"



text = input("enter the text: ")
word = input("enter the word to search: ")
print(search(text, word))
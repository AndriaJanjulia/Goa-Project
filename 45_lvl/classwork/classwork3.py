def search(text,word):
    if word in text:
        return "სიტყვა მოიძებნა"
    else:
        return "სიტყვა არ მოიძებნა"



text = input("enter the text: ")
word = input("enter the word to search: ")
print(search(text, word))
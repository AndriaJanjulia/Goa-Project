def count_words(text):
    words = text.split()
    return len(words)

text =input("შეიყვანეთ ტექსტი: ")

print("სიტყვების რაოდენობა:", count_words(text))
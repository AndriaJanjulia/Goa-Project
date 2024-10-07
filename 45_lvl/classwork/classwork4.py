def count_words(text):
    words = text.split()
    return len(words)

text =input("დაწერე კოდი: ")

print("ჩაწერე რიცხვი:", count_words(text))
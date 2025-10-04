import string
text = input("Nhập đoạn văn bản: ")
text = text.lower()
for ch in string.punctuation:
    text = text.replace(ch, "")
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("\nKết quả đếm từ:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")


text = input("Nhập một đoạn văn bản: ")
word = input("Nhập từ cần tìm: ")
text_lower = text.lower()
word_lower = word.lower()

count = text_lower.count(word_lower)

if count > 0:
    print(f"Từ '{word}' xuất hiện {count} lần trong đoạn văn bản.")
else:
    print(f"Từ '{word}' không xuất hiện trong đoạn văn bản.")


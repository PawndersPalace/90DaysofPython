sentence = "red blue red green blue red"
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1
for word, count in sorted(counts.items()):
    print(f"{word}: {count}")

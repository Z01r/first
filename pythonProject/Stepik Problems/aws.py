words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
d = []
for q in words:
    r = []
    for w in q:
        r.append(ord(w))
    d.append(r)
result = {words[i]: d[i] for i in range(len(words))}
print(result)

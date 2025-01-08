N = int(input())
words = []
for i in range(0, N):
  words.append(input())

unique_words = []
for i in words:
  if i not in unique_words:
    unique_words.append(i)

unique_words.sort(key = lambda x: (len(x), x))

for i in range(0, len(unique_words)):
  print(unique_words[i])
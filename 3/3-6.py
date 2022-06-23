#(Множества) Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

str_=[
    7,
    "Jack was hungry",
    "He walked to the kitchen.",
    "He got out some eggs.",
    "He took out some oil.",
    "He placed a skillet on the stove.",
    "Next, he turned on the heat.",
    "He poured the oil into the skillet."
      ]

n = str_[0]

words= set()
for i in range(n):
    words.update(str_[i + 1].strip(',').strip('.').strip().split())
print(len(words))
print(words)
word = input("Enter a word: ")
word = list(word)
j = 0
for i in range(len(word)):
    if j == len(word)-1:
        break
    if word[j] != word[j+1]:
        j += 1
        continue
    if word[j] == word[j+1]:
        word.pop(j)

print("".join(word))
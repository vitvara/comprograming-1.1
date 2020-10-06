import lesson_8

fin = open('lecture8\words.txt')
word_list = []
for line in fin:
    word = line.strip()
    word_list.append(word)
fin.close()

for word in word_list:
    print(lesson_8.is_abecedarian(word))

    pass
    # your code here

file = open("lecture8\words.txt")

for i in file:
    data = file.readline()
    if len(data)-1 <= 5:
        print(data[:-1])
        continue
file.close

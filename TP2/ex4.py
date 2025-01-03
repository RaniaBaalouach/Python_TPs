with open("numbers_letters.txt", "w") as file:
    file.write(" ".join(map(str, range(1, 21))) + "\n")
    file.write(" ".join(chr(i) for i in range(65, 91)))

with open("numbers_letters.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

with open("numbers_letters.txt", "r") as source, open("copy.txt", "w") as dest:
    dest.write(source.read())

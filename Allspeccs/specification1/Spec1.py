streamreader = open("text.txt", "r")
characters = {}
dictionary = {}
word = ""
file = ""
for line in streamreader:
    for character in line:
        character.lower()
        if ord(character) > 96 and ord(character) < 123:
            if character in characters:
                current_count = characters[character]
                characters[character] = str(int(current_count) + 1)
            else:
                characters[character] = "1"
        if character == " " or character == ".":
            if word == "":
                word += character
            else:
                if word in dictionary:
                    current_count = dictionary[word]
                    dictionary[word] = str(int(current_count) + 1)
                    for i in range(0, len(file)):
                        if file[i:i+len(word)] == word:
                            filelist = list(file)
                            filelist[i+len(word)+2] = current_count
                            file = ''.join(filelist)
                else:
                    dictionary[word] = "1"
                    file += word + ", 1 \n"
                word = ""
        else:
            word += character
streamreader.close()
streamwriter = open("csv.txt", "w")
streamwriter.write(file)

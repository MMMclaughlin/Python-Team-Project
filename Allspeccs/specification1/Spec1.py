streamreader = open("text.txt", "r")
characters = {}
dictionary = {}
word = ""
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
                else:
                    dictionary[word] = "1"
                word = ""
        else:
            word += character
streamreader.close()
streamwriter = open("csv.txt", "w")
streamwriter.write(str(dictionary))

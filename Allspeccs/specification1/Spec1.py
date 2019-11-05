import matplotlib.pyplot as plt

streamreader = open("text.txt", "r")
characters = {}
dictionary = {}
amount_of_values = 0
word = ""
file = ""
for line in streamreader:
    for character in line:
        # sets all characters to lower case so they can be analysed and so that a word with a capital letter isn't
        # counted separately to the same word without the capital letter
        character.lower()
        # checks the character being looked at is a letter
        if ord(character) > 96 and ord(character) < 123:
            # if the character being looked at is already in the characters list
            if character in characters:
                # increments the count of the relevant character
                characters[character] = str(int(characters[character]) + 1)
            else:
                characters[character] = "1"

        # if the character being looked at is the end of a word
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
                amount_of_values += 1
        else:
            word += character
streamreader.close()
streamwriter = open("csv.txt", "w")
streamwriter.write(file)
# creates the bar chart
plt.figure()
# plots each of the bars
values = list(dictionary.values())
values.sort()
plt.bar(dictionary.keys(), values)
# adds labels to each of the bars using the keys of the dictionary
plt.tight_layout()
# shows the bar chart
plt.show()

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
            if not word == "":
                # compares the new word to the dictionary of all recorded words
                if word in dictionary:
                    current_count = dictionary[word]
                    # increments the value associated to the word
                    dictionary[word] = str(int(current_count) + 1)
                    # go through the entire file
                    for i in range(0, len(file)):
                        # finds the position of the word within the file
                        if file[i:i+len(word)] == word:
                            # creates a list copy of the file as a string is immutable so you can't change individual
                            # characters but a list is mutable
                            filelist = list(file)
                            # moves along from the position of the key that has just been found to the position of the
                            # value and increments it
                            filelist[i+len(word)+2] = current_count
                            # resets file to nothing and then appends the list version of file to the end of the string
                            file = ''.join(filelist)
                else:
                    # creates the new key value pair in the dictionary
                    dictionary[word] = "1"
                    # adds the new key value pair to the file and creates a new line
                    file += word + ", 1 \n"
                word = ""
                amount_of_values += 1
        else:
            word += character
streamreader.close()
# writes the file string into the text file csv
streamwriter = open("csv.txt", "w")
streamwriter.write(file)
streamwriter.close()
# creates a bar chart
plt.figure()
# creates a list of all of the values in the dictionary
values = list(dictionary.values())
# orders the values as otherwise the bar chart values don't come out in numerical order
values.sort()
# plots each of the bars
plt.bar(dictionary.keys(), values)
# makes sure that the bar chart fits into the window 
plt.tight_layout()
# shows the bar chart
plt.show()
